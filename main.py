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
import os


if not os.path.exists("output"):
    os.makedirs("output")

# TODO: Use more functions to declutter the code (MD)

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
print("The golabal average:", average)

# 1. Import of the libraries we need for visualization
# 2. I looked up how to do visualization with a website that explains EDA for Python
# 3. Insert the function for a line chart and label it
# 4. I put a grid in the back and the dots at every "change point"

# Print how the global average total_ug_per_kg has changed over the years (1990-2018)
# %matplotlib inline

yearaverage = df.groupby("year")["total_ug_per_kg"].mean()

# Plot the line chart
ax = yearaverage.plot(marker="o", figsize=(10, 6))
plt.title("Average total µg/kg")
plt.xlabel("Year")
plt.ylabel("Average total µg/kg")
# Add value annotations
for x, y in zip(yearaverage.index, yearaverage.values):
    plt.text(x, y, f"{y:.1f}", ha="center", va="bottom", fontsize=9)
plt.grid(True)
plt.tight_layout()
plt.savefig("output/total_per_year.png")

# - Top Food Contributors:
#     - Which 3 food categories (product columns, e.g., fish, poultry, vegetables) show the highest average microplastic consumption (μg/kg) across all countries and years?
#     - Visualize the average microplastic content for the top 10 food categories.

"""
My roadmap: We calculate the average consumption for each food category. We put the averages and their related category name in a list. Then, I sort the list to get the top three food categories.
First, I need to define which columns are food columns (and not country names, year, and total consumption). I define variable 'food_columns' and put those columns in it.
I can calculate averages for each column. But, I need to save them somewhere, so that I can later compare the numbers. So, I first make a list, called 'mean_list'.
To add (append) each category and averages to the list, I use a for loop.
I sort this list by using sort() method. But, I need to define a key, such that the list can be sorted by the average numbers. If I don't do this, they will be sorted alphabetically by the category names.
Therefore, I define function sorting_by_avg(). This function returns the second items in our tuples, which are the average numbers.
"""

mean_list = []
def sorting_by_avg(key):
    return key[1]

food_columns = df.columns[2:-1]
for column in food_columns:
    mean_list.append([column, df[column].mean()])
mean_list.sort(key=sorting_by_avg, reverse=True)
print("3 food categories with the highest microplastic content:", mean_list[:3])

# Store names and averages of top 10 food categories for plotting (prevents loop from only showing the last item)
top_10_categories = [category for category, average in mean_list[:10]]
top_10_averages = [average for category, average in mean_list[:10]]

# plotting a bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_10_categories[::-1], top_10_averages[::-1])
plt.xlabel("Average Microplastic Consumption (μg/kg)")
plt.title("Top 10 Food Categories by Microplastic Content")
plt.tight_layout()
plt.savefig("output/average_consumption_top_10_food_categories.png")

# - Country-Level Totals:
#     - Which 5 countries have the highest average total_ug_per_kg over the entire period (1990-2018)?
#     - Which 5 countries have the lowest average total_ug_per_kg?

"""
Since what we need is over the entire period, we will group the data by the countries column, then focues on the column which we need (in this case: country and the avg_high_low_column) then we take the describe since it allows us to check more than one value (more modularity) and lastly we simply take the head x and tail x for the higest and lowest averages.
"""

avg_high_low_column = "total_ug_per_kg"
value_to_check = "mean"
number_of_high_low_countries = 5

df_high_low_countries = (
    df.groupby("country")[["country", avg_high_low_column]]
    .describe()[avg_high_low_column]
    .sort_values(by=value_to_check, ascending=False)[value_to_check]
)

highest_high_low_countries = df_high_low_countries.head(number_of_high_low_countries)

lowest_high_low_countries = df_high_low_countries.tail(number_of_high_low_countries)

print(
    "5 countries with the highest average consumption: \n",
    highest_high_low_countries,
    "\n 5 countries with the lowest average consumption: \n",
    lowest_high_low_countries,
)

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
plt.savefig("output/global_average_fruits.png")

# ## Intermediate Tasks

# - Detailed Food Category Analysis:
#     - For the top 3 food categories with the highest microplastic content, analyze their individual trends over time (1990-2018). Are some increasing more rapidly than others?
#     - Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1991) and latest (2018) years. Describe the shifts in contribution.

# Find out the total per year of all countries together for the top 3 food categories
top_3_columns = [category for category, avg in mean_list[:3]]
total_highest = df.groupby("year")[top_3_columns].sum()

# Plot a line chart to visualize the trends of each category
ax = total_highest.plot(marker="o", figsize=(10, 6))

plt.title("Microplastic content (1990-2018)")
plt.xlabel("Year")
plt.ylabel("Total µg/kg")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("output/intermediate_food_trends.png")

# Create a new dictionary for the results
results = {}

# Use slope to calculate the increase
for cat in top_3_columns[0:3]:
    y = total_highest[cat].values
    x = total_highest.index.values
    slope = np.polyfit(x, y, 1)[0]
    results[cat] = slope

# Make an order from fastest to slowest increase
print('\n Change in microplastic content of top 3 food categories from 1990 to 2018:\n')
sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
for cat, slope in sorted_results.items():
    print(f"{cat}: {slope:.2f} µg/kg per year")

print()

# Print the category with the fastest increase
fastest = max(results, key=results.get)
print(f"Fastest increase: {fastest} ({results[fastest]:.2f} µg/kg per year)")


# Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1990) and latest (2018) years

# Add the contribution of each country together and group only for 1990 and 2018
total_cat_year = df.groupby("year")[food_columns].sum().loc[[1990, 2018]]
total_per_year = df.groupby("year")["total_ug_per_kg"].sum().loc[[1990, 2018]]

# Calculate the contribution of each food to the total per year (1990, 2018) and give out in %

percentage_dec = total_cat_year.div(total_per_year, axis=0) * 100
percentage_p = percentage_dec.map(lambda x: f"{x:.2f}%")

# Extract data for 1990 and 2018 Daten
p_1990 = percentage_p.loc[1990].rename("1990")
p_2018 = percentage_p.loc[2018].rename("2018")

# Put them next to each other in comparison
p_compare = pd.concat([p_1990, p_2018], axis=1)
print('Contribution of food categories as a percentage of total (1990 and 2018) \n', p_compare)

# Describe the shifts in contribution / changes
change_dec = (
    (percentage_dec.loc[2018] - percentage_dec.loc[1990]) / percentage_dec.loc[1990]
) * 100
change_p = change_dec.map(lambda x: f"{x:.2f}%")

# Sort in decreasing order
change_dec_sorted = change_dec.sort_values(ascending=False)
change_p_sorted = change_dec_sorted.map(lambda x: f"{x:.2f}%")
print('Growth rate of the contribution of food categories to the total (1990 to 2018) \n', change_p_sorted)


# - Country-Specific Microplastic Profiles:
#     - Select two countries with significantly different average total_ug_per_kg (one high, one low, from your beginner analysis).
#     - For each selected country, visualize the breakdown of total_ug_per_kg by different food categories for the year 2018. Highlight the food categories contributing most to microplastic intake in these specific countries.
#
"""
## We need to limit our data to year of 2018 and only two countries. First I make a new data frame that contains all the data for the year 2018.
## I decided to get the countries with the highest and lowest averages, which we have from the beginner's questions.
## I make two other data frames, by restricting df_2018 to those country rows that I need.
## Then I drop the columns that I don't need (year, country, total_ug_per_kg).
## I also need to sort the values, but I couldn't simply do it by sort_values(), because I need to sort the data by a column. But here, I have many columns (each food category is one column). So, I need to swap the columns and rows. I do it with melt(). Now I can sort my values. Since this setting won't be saved in the original data, I need to put it into another variable.
"""

# restricing data to the year 2018
df_2018 = df[df["year"] == 2018]

# restricting the data to two countries with highest and lowest average consumption (Greece and Bangeladesh)
df_2018_high_country = df_2018[
    df_2018["country"] == highest_high_low_countries.index[0]
]
df_2018_low_country = df_2018[df_2018["country"] == lowest_high_low_countries.index[-1]]

# dropping the unwanted columns
df_foods_high_country = df_2018_high_country.drop(
    columns=["year", "country", "total_ug_per_kg"]
)
df_foods_low_country = df_2018_low_country.drop(
    columns=["year", "country", "total_ug_per_kg"]
)

# swapping rows and columns, and sorting the values
df_long_high = df_foods_high_country.melt()
df_long_high_sorted = df_long_high.sort_values(by="value")

df_long_low = df_foods_low_country.melt()
df_long_low_sorted = df_long_low.sort_values(by="value")


"""
Now I want a bar chart. I put each column into a list, so that I can plot them with plt.bar().
"""
# preparing x and y axis
high_country_food_category = df_long_high_sorted["variable"]
high_country_value = df_long_high_sorted["value"]

low_country_food_category = df_long_low_sorted["variable"]
low_country_value = df_long_low_sorted["value"]

"""
I want to highlight the food categories contributing most to microplastic intake in these specific countries.
I decided to highlight those categories with more than 100 ug per kg microplastic content.
For highlighting specific bars, I found out that I can create a list, containing a color for each bar in my plot.
But since I don't want to write everything manually, I use a for-loop and if.
Btw, since I have too many categories on the y-axis, I rotate lables so they don’t overlap.
"""

# plotting for the country with the highest microplastic intake
bar_colors_high = []

for v in high_country_value:
    if v >= 100:
        bar_colors_high.append("tab:red")
    else:
        bar_colors_high.append("tab:blue")

plt.figure(figsize=(12, 6))
plt.bar(high_country_food_category, high_country_value, color=bar_colors_high)
plt.xticks(rotation=90)
plt.title("Microplastic breakdown for Greece (2018)")
plt.xlabel("Food category")
plt.ylabel("Microplastics (µg/kg)")
plt.tight_layout()
plt.savefig("output/microplastic_breakdown_high_country")

# plotting for the country with the lowest microplastic intake
bar_colors_low = []

for v in low_country_value:
    if v >= 100:
        bar_colors_low.append("tab:red")
    else:
        bar_colors_low.append("tab:blue")

create_lineplot()
plt.figure(figsize=(12, 6))
plt.bar(low_country_food_category, low_country_value, color=bar_colors_low)
plt.xticks(rotation=90)
plt.title("Microplastic breakdown for Bangladesh (2018)")
plt.xlabel("Food category")
plt.ylabel("Microplastics (µg/kg)")
plt.tight_layout()
plt.savefig("output/microplastic_breakdown_low_country")


# - Growth Rate Analysis:
#     - Calculate the percentage increase in total_ug_per_kg from 1990 to 2018 for each country. Identify the top 5 countries with the highest growth rate in microplastic consumption.
#     - Investigate which food categories are driving this growth in those top 5 countries.

# Check whether the same number of years is represented for each country in the dataset
df["year"].value_counts()

# Focus on the relevant part of the dataframe for the growth rate analysis, namely start and end values for each country. Since not all countries have data for 1990, the earliest year was selected through .min() and assigned to the corresponding variable
first_year = df.groupby("country")["year"].min()

# The observation for 10 countries starts from 2010, whereas for 99 countries it starts from 1990
print('Number of countries with starting year 1990 or 2010: \n', first_year.value_counts())

# Make sure that all countries have a value for the year 2018 and assign it to the corresponding variable for later calculations
last_year = df.groupby("country")["year"].max()

# Prepare dataframes for calculations - extract start year values and align by the values in "country" and "year" columns
df_first = pd.merge(first_year, df, on=["country", "year"], how="left")
df_first = df_first[["country", "year", "total_ug_per_kg"]].rename(
    columns={"year": "first_year", "total_ug_per_kg": "first_value"}
)

# Prepare dataframes for calculations - extract end year values and align by the values in "country" and "year" columns
df_last = pd.merge(last_year, df, on=["country", "year"], how="left")
df_last = df_last[["country", "year", "total_ug_per_kg"]].rename(
    columns={"year": "last_year", "total_ug_per_kg": "last_value"}
)

# Merge the created dataframes
df_growth = pd.merge(df_first, df_last, on="country")

# Calculate growth rate (CAGR - compound growth rate)
df_growth["growth_rate"] = (df_growth["last_value"] / df_growth["first_value"]) ** (
    1 / (df_growth["last_year"] - df_growth["first_year"])
) - 1
# I used compound growth rate since it is less sensitive to variations. n is the Period (years)

# Sort values by growth_rate with ascending=False to extract the highest values first. head() outputs the top 5 countries with the highest growth rate
top_5_growth = df_growth.sort_values(ascending=False, by="growth_rate").head()

# Extract top 5 countries for later calculations and store them in a list
country_names = top_5_growth["country"].tolist()
print('Top 5 countries with the highest growth rate in microplastic consumption: ', country_names)

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
        start_value = df[
            (df["country"] == country) & (df["year"] == first_year[country])
        ][food].values[0]
        if start_value == 0:
            print(f"{country} - {food} starts at 0 in {first_year[country]}")

# Create a list to store the dictionaries resulting from the following CAGR and slope computation
results = list()

for country in country_names:
    for food in food_categories:
        food_start_value = df[
            (df["country"] == country) & (df["year"] == first_year[country])
        ][food].values[
            0
        ]  # Use .values[0] to extract the relevant value from the Series object
        food_end_value = df[
            (df["country"] == country) & (df["year"] == last_year[country])
        ][food].values[0]

        # In the following lines, I decided to calculate the CAGR and the slope for all combinations of countries and food categories.
        # The reason for this is that for some food categories, some countries have a food_start_value of 0, which would make the calculation of CAGR (dividing by 0) mathematically insensible.
        years = last_year[country] - first_year[country]
        slope = (
            food_end_value - food_start_value
        ) / years  # Slope as absolute change per year

        # Slope as % of final value per year
        if (
            food_end_value != 0
        ):  # If food_end_to_value is close to zero, the calculation of slope_percent can become meaningless
            slope_percent = (
                slope / food_end_value
            ) * 100  # Slope as percentage relative to final value
        else:
            slope_percent = np.nan

        # CAGR only if start_value > 0, else NaN to avoid "RuntimeWarning: divide by zero encountered in scalar divide"
        if food_start_value > 0 and food_end_value >= 0:
            cagr = (food_end_value / food_start_value) ** (1 / years) - 1
        else:
            cagr = np.nan

        results.append(
            {
                "country": country,
                "food_category": food,
                "food_start_value": food_start_value,
                "food_end_value": food_end_value,
                "period_in_years": years,
                "slope_per_year": slope,
                "slope_percent_per_year": slope_percent,
                "CAGR": cagr,
            }
        )

# Create a dataframe based on the results
df_growth_rates = pd.DataFrame(results)

# Pivot to extract per-country information about the CAGR and slope values in each food category
growth_pivot_df = df_growth_rates.pivot(
    index="country", columns="food_category", values=["CAGR", "slope_percent_per_year"]
)

# Extract top 3 contributing food categories by CAGR
top_drivers_cagr = (
    df_growth_rates.sort_values(["country", "CAGR"], ascending=[True, False])
    .groupby("country")
    .head(3)
)

# Extract top 3 contributing food categories by slope percentage
top_drivers_slope = (
    df_growth_rates.sort_values(
        ["country", "slope_percent_per_year"], ascending=[True, False]
    )
    .groupby("country")
    .head(3)
)

"""
Correlation between Food Groups (Optional/Advanced):
    - Is there a correlation between microplastic content in different food groups? For example, do countries with high microplastic in fish also tend to have high microplastic in seafood or processed_foods? Use correlation matrices or scatter plots to explore.
"""

# Get the correlation matrix
df.corr

# define a vairable with the correlation regardint numerics only.
corr = df.corr(method="pearson", min_periods=1, numeric_only=True)

# define a variable to check the correlation with regards to it
corr_check_col = "total_ug_per_kg"

# Extract correlations with 'A' since it is always 1
corr_with_A = corr[corr_check_col].drop(corr_check_col)

# Plot as horizontal bar chart, since a vertical bar in this case makes lees sense and is harder on the eyes to follow
plt.figure()
corr_with_A.sort_values().plot(kind="barh", color="skyblue", edgecolor="black")
plt.title(f"Correlation of {corr_check_col} with Other Variables")
plt.xlabel("Correlation Coefficient")
plt.ylabel("Variables")
plt.tight_layout()
plt.savefig("output/intermediate_correlation_of_microplastics.png")


# ### Public Health Implications & Recommendations (Qualitative):
# - Based on your findings, what are 2-3 key insights you would present to the PurePlate Initiative regarding microplastic consumption?
# - Propose potential policy recommendations or public awareness strategies that could help reduce human exposure to microplastics through diet, citing evidence from your analysis.
#
# > Remember to provide clear visualizations and concise explanations for all your findings. Your analysis will contribute directly to a vital public health discussion!
#
