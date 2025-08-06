# - Data Loading and Initial Exploration:
#     - Load the dataset into a pandas DataFrame.
#     - Display the first 5 rows and check the data types of all columns.
#     - Identify and handle any missing values.
#     - List all unique Country values in the dataset.

# Basic command
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

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

# - Country-Level Totals:
#     - Which 5 countries have the highest average total_ug_per_kg over the entire period (1990-2018)?
#     - Which 5 countries have the lowest average total_ug_per_kg?

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

# - Correlation between Food Groups (Optional/Advanced):
#     - Is there a correlation between microplastic content in different food groups? For example, do countries with high microplastic in fish also tend to have high microplastic in seafood or processed_foods? Use correlation matrices or scatter plots to explore.
# 

# ### Public Health Implications & Recommendations (Qualitative):
# - Based on your findings, what are 2-3 key insights you would present to the PurePlate Initiative regarding microplastic consumption?
# - Propose potential policy recommendations or public awareness strategies that could help reduce human exposure to microplastics through diet, citing evidence from your analysis.
# 
# > Remember to provide clear visualizations and concise explanations for all your findings. Your analysis will contribute directly to a vital public health discussion!
# 


