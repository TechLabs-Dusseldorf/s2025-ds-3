# Basic imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# - Data Loading and Initial Exploration:
#     - Load the dataset into a pandas DataFrame.
#     - Display the first 5 rows and check the data types of all columns.
#     - Identify and handle any missing values.
#     - List all unique Country values in the dataset.

def load_and_inspect_data(filepath):
    df = pd.read_csv(filepath)
    print("\n")
    print("Taking a first look at the dataset:\n",
          df.head())
    print("Data types:\n",
          df.dtypes)
    print("\n")
    print("Checking for null values...\n",
    "Null values found:\n", df.isnull().sum())
    print("\n")
    print("Checking for NaN values...\n",
          "NaN values found:\n", df.isna().sum())
    print("\n")
    countries_list = df["country"].unique()
    print("Countries represented in the dataset:\n")
    for country_idx, country_name in enumerate(countries_list):
        print(country_idx, country_name)
    
    return df

# Beginner Task

# - Overall Trends in Microplastic Consumption:
# - What is the average total_ug_per_kg across all countries and years in the dataset?
# - How has the global average total_ug_per_kg changed over the years (1990-2018)? Visualize this trend.

def calculate_and_plot_global_average_total_ug_kg(df, year_col, total_ug_per_kg_col):
    yearly_average = df.groupby(year_col)[total_ug_per_kg_col].mean()
    print("The average total_ug_per_kg across all countries and years is:\n", yearly_average)

    ax = yearly_average.plot(marker='o', figsize=(10, 6))
    plt.title("Average total µg/kg over years")
    plt.xlabel("Year")
    plt.ylabel("Average total µg/kg")
    plt.grid(True)
    plt.tight_layout()
    # Add value annotations on each data point
    for x, y in zip(yearly_average.index, yearly_average.values):
        plt.text(x, y + 13, f'{y:.1f}', ha='center', va='bottom', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return yearly_average

# - Country-Level Totals:
    #     - Which 5 countries have the highest average total_ug_per_kg over the entire period (1990-2018)?
    #     - Which 5 countries have the lowest average total_ug_per_kg?

# - Initial Time-Series for a Food Category:
#     - Choose one of the top 3 food categories identified in question 3. How has the microplastic content in this specific food category changed over time (1990-2018) globally? Visualize this trend.

def plot_food_category_trend(df, food_category_col):
    # Group by year and calculate mean for the specified food category
    trend_data = df.groupby("year")[food_category_col].mean().reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=trend_data, x="year", y=food_category_col, marker="o")
    plt.title(f"Global Average Microplastic Content in {food_category_col.capitalize()} (1990–2018)", fontsize=14)
    plt.xlabel("Year")
    plt.ylabel("Microplastic Content (μg/kg)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Intermediate Task
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

def analyze_growth_rate(df, start_year=None, end_year=2018, top_n_countries=5, top_n_food_categories=3):
    # Determine earliest year per country if start_year not provided
    if start_year is None:
        first_year = df.groupby("country")["year"].min().rename("first_year").reset_index()
    else:
        first_year = pd.Series(start_year, index=df["country"].unique(), name="first_year").reset_index()
        first_year.columns = ["country", "first_year"]

    df_first = pd.merge(first_year, df, 
                        left_on=["country", "first_year"], right_on=["country", "year"], how="left")
    df_first = df_first[["country", "first_year", "total_ug_per_kg"]].rename(columns={"first_year": "year", "total_ug_per_kg": "first_value"})

    # Get last year per country (or use fixed end_year if specified)
    if end_year is None:
        last_year = df.groupby("country")["year"].max().rename("last_year").reset_index()
    else:
        last_year = pd.Series(end_year, index=df["country"].unique(), name="last_year").reset_index()
        last_year.columns = ["country", "last_year"]

    df_last = pd.merge(last_year, df, 
                       left_on=["country", "last_year"], right_on=["country", "year"], how="left")
    df_last = df_last[["country", "last_year", "total_ug_per_kg"]].rename(columns={"last_year": "year", "total_ug_per_kg": "last_value"})

    # Merge for growth calculation
    df_growth = pd.merge(df_first, df_last, on="country")
    df_growth["period_years"] = df_growth["year_y"] - df_growth["year_x"]

    # CAGR calculation with safety checks to avoid division by zero
    df_growth["growth_rate"] = np.where(
        (df_growth["first_value"] > 0) & (df_growth["period_years"] > 0),
        (df_growth["last_value"] / df_growth["first_value"]) ** (1 / df_growth["period_years"]) - 1,
        np.nan
    )

    # Get top N countries by growth_rate
    top_growth = df_growth.sort_values("growth_rate", ascending=False).head(top_n_countries)
    top_countries = top_growth["country"].tolist()

    # Identify food columns (excluding country, year, total_ug_per_kg)
    food_categories = [col for col in df.columns if col not in ["country", "year", "total_ug_per_kg"]]

    # Prepare results container
    results = []

    for country in top_countries:
        start_y = first_year.loc[first_year["country"] == country, "first_year"].values[0]
        end_y = last_year.loc[last_year["country"] == country, "last_year"].values[0]
        years = end_y - start_y
        
        for food in food_categories:
            start_val = df.loc[(df["country"] == country) & (df["year"] == start_y), food].values
            end_val = df.loc[(df["country"] == country) & (df["year"] == end_y), food].values
            
            if len(start_val) == 0 or len(end_val) == 0:
                continue
            start_val = start_val[0]
            end_val = end_val[0]

            slope = (end_val - start_val) / years if years > 0 else np.nan
            slope_percent = (slope / end_val) * 100 if end_val != 0 else np.nan
            
            if start_val > 0 and end_val >= 0 and years > 0:
                cagr = (end_val / start_val) ** (1 / years) - 1
            else:
                cagr = np.nan

            results.append({
                "country": country,
                "food_category": food,
                "start_year": start_y,
                "end_year": end_y,
                "start_value": start_val,
                "end_value": end_val,
                "period_years": years,
                "slope_per_year": slope,
                "slope_percent_per_year": slope_percent,
                "CAGR": cagr,
            })


    df_growth_rates = pd.DataFrame(results)

    # Pivot for convenience: CAGR and slope percent per food category by country
    growth_pivot = df_growth_rates.pivot(index="country", columns="food_category", values=["CAGR", "slope_percent_per_year"])

    # Extract top food categories by CAGR and slope percent per country
    top_drivers_cagr = df_growth_rates.sort_values(["country", "CAGR"], ascending=[True, False]).groupby("country").head(top_n_food_categories)
    top_drivers_slope = df_growth_rates.sort_values(["country", "slope_percent_per_year"], ascending=[True, False]).groupby("country").head(top_n_food_categories)

    return {
        "top_countries_growth": top_growth,
        "top_drivers_cagr": top_drivers_cagr,
        "top_drivers_slope": top_drivers_slope,
        "growth_pivot": growth_pivot,
    }

# - Correlation between Food Groups (Optional/Advanced):
#     - Is there a correlation between microplastic content in different food groups? For example, do countries with high microplastic in fish also tend to have high microplastic in seafood or processed_foods? Use correlation matrices or scatter plots to explore.
# 

# ### Public Health Implications & Recommendations (Qualitative):
# - Based on your findings, what are 2-3 key insights you would present to the PurePlate Initiative regarding microplastic consumption?
# - Propose potential policy recommendations or public awareness strategies that could help reduce human exposure to microplastics through diet, citing evidence from your analysis.
# 
# > Remember to provide clear visualizations and concise explanations for all your findings. Your analysis will contribute directly to a vital public health discussion!
#

def main():
    if len(sys.argv) < 2:
        print("Please provide the filepath as an argument.")
        sys.exit(1)
    filepath = sys.argv[1]
    df = load_and_inspect_data(filepath)
    print("\n")
    calculate_and_plot_global_average_total_ug_kg(df, "year", "total_ug_per_kg")

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
        mean_list.append((column, df[column].mean()))
    mean_list.sort(key=sorting_by_avg, reverse=True)

    print("Top 3 food categories:")
    for category, average in mean_list[:3]:
        print(f"{category}: {average:.2f} μg/kg")

    top_3_food_categories = mean_list[:3]
    top_10_categories = [category for category, average in mean_list[:10]]
    top_10_averages = [average for category, average in mean_list[:10]]

    plt.figure(figsize=(10, 6))
    plt.barh(top_10_categories[::-1], top_10_averages[::-1])
    plt.xlabel('Average Microplastic Consumption (μg/kg)')
    plt.title('Top 10 Food Categories by Microplastic Content')
    plt.tight_layout()
    plt.show()

    print("\n")
    plot_food_category_trend(df, "total_milk")

# - Detailed Food Category Analysis:
#     - For the top 3 food categories with the highest microplastic content, analyze their individual trends over time (1990-2018). Are some increasing more rapidly than others?
#     - Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1991) and latest (2018) years. Describe the shifts in contribution.

    # Find out the total per year of all countries together for the top 3 food categories
    # Extract just the column names from the top 3 tuples
    top_3_columns = [category for category, avg in top_3_food_categories[:3]]

    total_highest = df.groupby("year")[top_3_columns].sum()


    # Plot a line chart to visualize the trends of each category
    ax = total_highest.plot(marker='o', figsize=(10, 6))

    plt.title("Microplastic content (1990-2018)")
    plt.xlabel("Year")
    plt.ylabel("Total µg/kg")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


    # Create a new dictionary for the results
    results = {}

    #Use slope to calculate the increase
    for cat in top_3_columns[0:3]:
        y = total_highest[cat].values
        x = total_highest.index.values
        slope = np.polyfit(x, y, 1)[0]
        results[cat] = slope

    # Make an order from fastest to slowest increase
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

    # Calculate the contribution of each food to the total per year (1990, 2018) and give out in %

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
    
    print("\n")
    results = analyze_growth_rate(df)

    print("Top countries by growth rate:\n")
    print(results["top_countries_growth"])
    print("\n")

    print("\n")
    print("Top 3 food contributors by CAGR in top countries:\n")
    print(results["top_drivers_cagr"])
    print("\n")

    print("\n")
    print("Top 3 food contributors by slope % in top countries:\n")
    print(results["top_drivers_slope"])
    print("\n")

if __name__ == "__main__":
    main()