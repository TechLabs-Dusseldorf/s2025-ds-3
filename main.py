# - Data Loading and Initial Exploration:
#     - Load the dataset into a pandas DataFrame.
#     - Display the first 5 rows and check the data types of all columns.
#     - Identify and handle any missing values.
#     - List all unique Country values in the dataset.
# 

# Basic imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

#TODO: Use more functions to declutter the code (MD)

# Open the File as a DataFram
df = pd.read_csv(r"./processed_microplastics.csv")

# First insights into the dataset
df.head(5)

# Check data type for each column
df.dtypes

# Check for any missing values - none found
df.isnull().sum()

# Drop NaN values - not necessary here because no such value was found
df = df.dropna()

# Print unique values for the column "country"
df["country"].unique()

# ## Beginner Task

# - Overall Trends in Microplastic Consumption:
#     - What is the average total_ug_per_kg across all countries and years in the dataset?
#     - How has the global average total_ug_per_kg changed over the years (1990-2018)? Visualize this trend.

# Print the golabal average total_ug_per_kg
average = df["total_ug_per_kg"].mean()
print(average)

# 1. Import of the libraries we need for visualization
# 2. I looked up how to do visualization with a website that explains EDA for Python
# 3. Insert the function for a line chart and label it
# 4. I put a grid in the back and the dots at every "change point"

# Print how the global average total_ug_per_kg has changed over the years (1990-2018)
#%matplotlib inline

yearaverage = df.groupby("year")["total_ug_per_kg"].mean()

# Plot the line chart
ax = yearaverage.plot(marker='o', figsize=(10, 6))
plt.title("Average total µg/kg")
plt.xlabel("Year")
plt.ylabel("Average total µg/kg")


# Add value annotations
for x, y in zip(yearaverage.index, yearaverage.values):
    plt.text(x, y, f'{y:.1f}', ha='center', va='bottom', fontsize=9)

plt.grid(True)
plt.tight_layout()
plt.show()

# - Top Food Contributors:
#     - Which 3 food categories (product columns, e.g., fish, poultry, vegetables) show the highest average microplastic consumption (μg/kg) across all countries and years?
#     - Visualize the average microplastic content for the top 10 food categories.

# My roadmap: We calculate the average consumption for each food category. We put the averages and their related category name in a list. Then, I sort the list to get the top three food categories.
# First, I need to define which columns are food columns (and not country names, year, and total consumption). I define variable 'food_columns' and put those columns in it.
# I can calculate averages for each column. But, I need to save them somewhere, so that I can later compare the numbers. So, I first make a list, called 'mean_list'.
# But, at the end I want to have the names of food categories, not the average numbers themselves. I decided to make a tuple, which consists of column names and average consumption.
# To add (append) each category and averages to the list, I use a for loop.
# I sort this list by using sort() method. But, I need to define a key, such that the list can be sorted by the average numbers. If I don't do this, they will be sorted alphabetically by the category names.
# Therefore, I define function sorting_by_avg(). This function returns the second items in our tuples, which are the average numbers.

mean_list = []
def sorting_by_avg(key):
    return key[1]

food_columns = df.columns[2:-1]
for column in food_columns:
    mean_list.append([column, df[column].mean()])
mean_list.sort(key = sorting_by_avg, reverse=True)

for category, average in mean_list[:3]:
    print(category)

# Store names and averages of top 10 food categories for plotting (prevents loop from only showing the last item)
top_10_categories = [category for category, average in mean_list[:10]]
top_10_averages = [average for category, average in mean_list[:10]]

# plotting a bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_10_categories[::-1], top_10_averages[::-1])
plt.xlabel('Average Microplastic Consumption (μg/kg)')
plt.title('Top 10 Food Categories by Microplastic Content')
plt.tight_layout()
plt.show()

# - Country-Level Totals:
#     - Which 5 countries have the highest average total_ug_per_kg over the entire period (1990-2018)?
#     - Which 5 countries have the lowest average total_ug_per_kg?

"""
Since what we need is over the entire period, we will groub the Data by the countries column, then focues on the column which we need (in this case: country and the avg_high_low_column) then we take the describe since it allows us to check more than one value (more modularity) and lastly we simply take the head x and tail x for the higest and lowest averages.
"""

avg_high_low_column = 'total_ug_per_kg'
value_to_check = 'mean'
number_of_high_low_countries = 5

df_high_low_countries = df.groupby('country')[['country', avg_high_low_column]].describe()[avg_high_low_column].sort_values(by=value_to_check, ascending=False)[value_to_check]

highest_high_low_countries = df_high_low_countries.head(number_of_high_low_countries)

lowest_high_low_countries = df_high_low_countries.tail(number_of_high_low_countries)


# - Initial Time-Series for a Food Category:
#     - Choose one of the top 3 food categories identified in question 3. How has the microplastic content in this specific food category changed over time (1990-2018) globally? Visualize this trend.

# The food category "fruits" is selected and the dataframe is grouped by years so that these values can serve as x-axis
fruits_trend = df.groupby("year")["fruits"].median().reset_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.lineplot(data=fruits_trend, x="year", y="fruits", marker="o")
plt.title("Global Average Microplastic Content in Fruits (1990–2018)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Microplastic Content (μg/kg)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ## Intermediate Task

# - Detailed Food Category Analysis:
#     - For the top 3 food categories with the highest microplastic content, analyze their individual trends over time (1990-2018). Are some increasing more rapidly than others?
#     - Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1991) and latest (2018) years. Describe the shifts in contribution.

#Find out the total per year of all countries together for the top 3 food categories
total_highest = df.groupby("year")[top_categories[0:3]].sum()

#Plot a line chart to visualize the trends of each category
ax = total_highest.plot(marker='o', figsize=(10, 6))

plt.title("Microplastic content (1990-2018)")
plt.xlabel("Year")
plt.ylabel("Total µg/kg")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


#Create a new dictionary for the results
results = {}

#Use slope to calculate the increase
for cat in top_categories[0:3]:
    y = total_highest[cat].values
    x = total_highest.index.values
    slope = np.polyfit(x, y, 1)[0]
    results[cat] = slope

#Make an order from fastest to slowest increase
sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
for cat, slope in sorted_results.items():
    print(f"{cat}: {slope:.2f} µg/kg per year")

print()

#Print the category with the fastest increase
fastest = max(results, key=results.get)
print(f"Fastest increase: {fastest} ({results[fastest]:.2f} µg/kg per year)")


# Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1990) and latest (2018) years

#Filter the food columns (first 2 columns and last column are no food)
food_cols = df.columns[2:-1]

#Add the contribution of each country together and group only for 1990 and 2018
total_cat_year = df.groupby("year")[food_cols].sum().loc[[1990, 2018]]
total_per_year =  df.groupby("year")["total_ug_per_kg"].sum().loc[[1990, 2018]]

#Calculate the contribution of each food to the total per year (1990, 2018) and give out in %

percentage_dec = total_cat_year.div(total_per_year, axis=0) * 100
percentage_p = percentage_dec.applymap(lambda x: f"{x:.2f}%")

# Extract data for 1990 and 2018 Daten
p_1990 = percentage_p.loc[1990].rename("1990")
p_2018 = percentage_p.loc[2018].rename("2018")

# Put them next to each other in comparison 
p_compare = pd.concat([p_1990, p_2018], axis=1)
print(p_compare)

# Describe the shifts in contribution / changes
change_dec = ((percentage_dec.loc[2018] - percentage_dec.loc[1990]) / percentage_dec.loc[1990]) * 100
change_p = change_dec.map(lambda x: f"{x:.2f}%")

# Sort in decreasing order 
change_dec_sorted = change_dec.sort_values(ascending=False)
change_p_sorted = change_dec_sorted.map(lambda x: f"{x:.2f}%")
print(change_p_sorted)


# - Country-Specific Microplastic Profiles:
#     - Select two countries with significantly different average total_ug_per_kg (one high, one low, from your beginner analysis).
#     - For each selected country, visualize the breakdown of total_ug_per_kg by different food categories for the year 2018. Highlight the food categories contributing most to microplastic intake in these specific countries.
# 

# - Growth Rate Analysis:
#     - Calculate the percentage increase in total_ug_per_kg from 1990 to 2018 for each country. Identify the top 5 countries with the highest growth rate in microplastic consumption.
#     - Investigate which food categories are driving this growth in those top 5 countries.

# Check whether the same number of years is represented for each country in the dataset
df["year"].value_counts()

# Focus on the relevant part of the dataframe for the growth rate analysis, namely start and end values for each country. Since not all countries have data for 1990, the earliest year was selected through .min() and assigned to the corresponding variable
first_year = df.groupby("country")["year"].min()

# The observation for 10 countries starts from 2010, whereas for 99 countries it starts from 1990
print(first_year.value_counts())

# Make sure that all countries have a value for the year 2018 and assign it to the corresponding variable for later calculations
last_year = df.groupby("country")["year"].max()

# Prepare dataframes for calculations - extract start year values and align by the values in "country" and "year" columns
df_first = pd.merge(first_year, df, on=["country", "year"], how="left")
df_first = df_first[["country", "year", "total_ug_per_kg"]].rename(columns={"year": "first_year", "total_ug_per_kg": "first_value"})

# Prepare dataframes for calculations - extract end year values and align by the values in "country" and "year" columns
df_last = pd.merge(last_year, df, on=["country", "year"], how="left")
df_last = df_last[["country", "year", "total_ug_per_kg"]].rename(columns={"year": "last_year", "total_ug_per_kg": "last_value"})

# Merge the created dataframes
df_growth = pd.merge(df_first, df_last, on="country")

# Calculate growth rate (CAGR - compound growth rate)
df_growth["growth_rate"] = (((df_growth["last_value"] / df_growth["first_value"]) ** (1 / (df_growth["last_year"] - df_growth["first_year"])) - 1))
# I used compound growth rate since it is less sensitive to variations. n is the Period (years)

# Sort values by growth_rate with ascending=False to extract the highest values first. head() outputs the top 5 countries with the highest growth rate
top_5_growth = df_growth.sort_values(ascending=False, by="growth_rate").head()

# Extract top 5 countries for later calculations and store them in a list
country_names = top_5_growth["country"].tolist()
print(country_names)

# Filter the dataset with .isin() to get the relevant values for the 5 countries
df_top_countries = df[df["country"].isin(country_names)]

# Extract food categories for later calculations and store them in a list
food_categories = list()

for col_name in df.columns:
    if col_name not in ["year", "total_ug_per_kg", "country"]:
        food_categories.append(col_name)

# Check whether some countries have a first_year values of 0. This is important to know, since the CAGR calculation needs a denominator which is greater than 0.
for country in country_names:
    for food in food_categories:
        start_value = df[(df["country"] == country) & (df["year"] == first_year[country])][food].values[0]
        if start_value == 0:
            print(f"{country} - {food} starts at 0 in {first_year[country]}")

# Create a list to store the dictionaries resulting from the following CAGR and slope computation
results = list()

for country in country_names:
    for food in food_categories:
        food_start_value = df[(df["country"] == country) & (df["year"] == first_year[country])][food].values[0] # Use .values[0] to extract the relevant value from the Series object
        food_end_value = df[(df["country"] == country) & (df["year"] == last_year[country])][food].values[0]

        # In the following lines, I decided to calculate the CAGR and the slope for all combinations of countries and food categories.
        # The reason for this is that for some food categories, some countries have a food_start_value of 0, which would make the calculation of CAGR (dividing by 0) mathematically insensible.
        years = last_year[country] - first_year[country]
        slope = (food_end_value - food_start_value) / years # Slope as absolute change per year

        # Slope as % of final value per year
        if food_end_value != 0: # If food_end_to_value is close to zero, the calculation of slope_percent can become meaningless
            slope_percent = (slope / food_end_value) * 100 # Slope as percentage relative to final value
        else:
            slope_percent = np.nan

        # CAGR only if start_value > 0, else NaN to avoid "RuntimeWarning: divide by zero encountered in scalar divide"
        if food_start_value > 0 and food_end_value >= 0:
            cagr = (food_end_value / food_start_value) ** (1 / years) - 1
        else:
            cagr = np.nan

        results.append({"country": country,
                        "food_category": food,
                        "food_start_value": food_start_value,
                        "food_end_value": food_end_value,
                        "period_in_years": years,
                        "slope_per_year": slope,
                        "slope_percent_per_year": slope_percent,
                        "CAGR": cagr,
                        })

# Create a dataframe based on the results
df_growth_rates = pd.DataFrame(results)

# Pivot to extract per-country information about the CAGR and slope values in each food category
growth_pivot_df = df_growth_rates.pivot(index="country", 
                                 columns="food_category", 
                                 values=["CAGR", "slope_percent_per_year"])

# Extract top 3 contributing food categories by CAGR
top_drivers_cagr = df_growth_rates.sort_values(["country", "CAGR"], ascending=[True, False]).groupby("country").head(3)

# Extract top 3 contributing food categories by slope percentage
top_drivers_slope = df_growth_rates.sort_values(["country", "slope_percent_per_year"], ascending=[True, False]).groupby("country").head(3)

"""
Correlation between Food Groups (Optional/Advanced):
    - Is there a correlation between microplastic content in different food groups? For example, do countries with high microplastic in fish also tend to have high microplastic in seafood or processed_foods? Use correlation matrices or scatter plots to explore.
"""

# Get the correlation matrix
df.corr

# define a vairable with the correlation regardint numerics only.
corr = df.corr(method='pearson', min_periods=1, numeric_only=True)

# define a variable to check the correlation with regards to it
corr_check_col = 'total_ug_per_kg'

# Extract correlations with 'A' since it is always 1
corr_with_A = corr[corr_check_col].drop(corr_check_col)

# Plot as horizontal bar chart, since a vertical bar in this case makes lees sense and is harder on the eyes to follow
corr_with_A.sort_values().plot(kind="barh", color="skyblue", edgecolor="black")
plt.title(f"Correlation of {corr_check_col} with Other Variables")
plt.xlabel("Correlation Coefficient")
plt.ylabel("Variables")
plt.show()


# ### Public Health Implications & Recommendations (Qualitative):
# - Based on your findings, what are 2-3 key insights you would present to the PurePlate Initiative regarding microplastic consumption?
# - Propose potential policy recommendations or public awareness strategies that could help reduce human exposure to microplastics through diet, citing evidence from your analysis.
# 
# > Remember to provide clear visualizations and concise explanations for all your findings. Your analysis will contribute directly to a vital public health discussion!
# 

