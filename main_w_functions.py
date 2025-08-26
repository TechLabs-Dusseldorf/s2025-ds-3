# Basic imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import pycountry_convert as pc



if not os.path.exists("output"):
    os.makedirs("output")


"""
- Data Loading and Initial Exploration:
    - Load the dataset into a pandas DataFrame.
    - Display the first 5 rows and check the data types of all columns.
    - Identify and handle any missing values.
    - List all unique Country values in the dataset.
"""


def load_and_inspect_data(filepath):
    df = pd.read_csv(filepath)
    print("\n")
    print("Taking a first look at the dataset:\n", df.head())
    print("Data types:\n", df.dtypes)
    print("\n")
    print("Checking for null values...\n", "Null values found:\n", df.isnull().sum())
    print("\n")
    print("Checking for NaN values...\n", "NaN values found:\n", df.isna().sum())
    print("\n")
    countries_list = df["country"].unique()
    print("Countries represented in the dataset:\n")
    for country_idx, country_name in enumerate(countries_list):
        print(country_idx, country_name)

    return df


"""
Beginner Tasks:
"""


"""
- Overall Trends in Microplastic Consumption:
    - What is the average total_ug_per_kg across all countries and years in the dataset?
    - How has the global average total_ug_per_kg changed over the years (1990-2018)? Visualize this trend.
"""


def calculate_and_plot_global_average_total_ug_kg(df, year_col, total_ug_per_kg_col):
    yearly_average = df.groupby(year_col)[total_ug_per_kg_col].mean()
    print(
        "The average total_ug_per_kg across all countries and years is:\n",
        yearly_average,
    )

    ax = yearly_average.plot(marker="o", figsize=(10, 6))
    plt.title("Average Total µg/kg Across All Countries from 1990 to 2018")
    plt.xlabel("Year")
    plt.ylabel("Average Total µg/kg")
    plt.grid(True)
    plt.tight_layout()
    # Add value annotations on each data point
    for x, y in zip(yearly_average.index, yearly_average.values):
        plt.text(x, y + 13, f"{y:.1f}", ha="center", va="bottom", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/1_total_per_year.png")

    return yearly_average


"""
- Top Food Contributors:
    - Which 3 food categories (product columns, e.g., fish, poultry, vegetables) show the highest average microplastic consumption (μg/kg) across all countries and years?
    - Visualize the average microplastic content for the top 10 food categories.
"""

"""
My roadmap: We calculate the average consumption for each food category. We put the averages and their related category name in a list. Then, I sort the list to get the top three food categories.
First, I need to define which columns are food columns (and not country names, year, and total consumption). I define variable 'food_columns' and put those columns in it.
I can calculate averages for each column. But, I need to save them somewhere, so that I can later compare the numbers. So, I first make a list, called 'mean_list'.
To add (append) each category and averages to the list, I use a for loop.
I sort this list by using sort() method. But, I need to define a key, such that the list can be sorted by the average numbers. If I don't do this, they will be sorted alphabetically by the category names.
Therefore, I define function sorting_by_avg(). This function returns the second items in our tuples, which are the average numbers.
"""


def calculate_top_n_contaminated_categories(df, n, start_food_col, end_food_col):
    mean_list = []

    def sorting_by_avg(key):
        return key[1]

    food_columns = df.columns[start_food_col:end_food_col]
    for column in food_columns:
        mean_list.append([column, df[column].mean()])
    mean_list.sort(key=sorting_by_avg, reverse=True)
    print("\nThree food categories with the highest microplastic content: \n", mean_list[:n])
    return mean_list


def plot_top_n_contaminated_categories(df, n, mean_list):
    # Store names and averages of top n food categories for plotting (prevents loop from only showing the last item)
    top_n_categories = [category for category, average in mean_list[:n]]
    top_n_averages = [average for category, average in mean_list[:n]]

    # plotting a bar chart
    plt.figure(figsize=(10, 6))
    plt.barh(top_n_categories[::-1], top_n_averages[::-1])
    plt.xlabel("Average Microplastic Consumption (μg/kg)")
    plt.title("Top Food Categories by Microplastic Content")
    plt.tight_layout()
    plt.savefig("output/2_average_consumption_top_n_food_categories.png")

    return top_n_categories


"""
- Country-Level Totals:
    - Which 5 countries have the highest average total_ug_per_kg over the entire period (1990-2018)?
    - Which 5 countries have the lowest average total_ug_per_kg?
"""


"""
Since what we need is over the entire period, we will group the data by the countries column, then focues on the column which we need (in this case: country and the avg_high_low_column) then we take the describe since it allows us to check more than one value (more modularity) and lastly we simply take the head x and tail x for the higest and lowest averages.
"""


def highest_lowest_high_low_countries(
    df: pd.DataFrame,
    avg_high_low_column: str,
    value_to_check: str,
    number_of_high_low_countries: int,
):
    df_high_low_countries = (
        df.groupby("country")[["country", avg_high_low_column]]
        .describe()[avg_high_low_column]
        .sort_values(by=value_to_check, ascending=False)[value_to_check]
    )

    highest_high_low_countries = df_high_low_countries.head(
        number_of_high_low_countries
    )

    lowest_high_low_countries = df_high_low_countries.tail(number_of_high_low_countries)

    print(
        "5 countries with the highest average consumption: \n",
        highest_high_low_countries,
        "\n\n 5 countries with the lowest average consumption: \n",
        lowest_high_low_countries,
    )
    return (highest_high_low_countries, lowest_high_low_countries)


"""
- Initial Time-Series for a Food Category:
    - Choose one of the top 3 food categories identified in question 3. How has the microplastic content in this specific food category changed over time (1990-2018) globally? Visualize this trend.
"""


def plot_food_category_trend(df, food_category_col):
    # Group by year and calculate mean for the specified food category
    trend_data = df.groupby("year")[food_category_col].mean().reset_index()

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=trend_data, x="year", y=food_category_col, marker="o")
    plt.title(
        f"Global Average Microplastic Content in {food_category_col.capitalize()} (1990–2018)",
        fontsize=14,
    )
    plt.xlabel("Year")
    plt.ylabel("Microplastic Content (μg/kg)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/3_global_average_one_category.png")


"""
Intermediate Tasks
"""


"""
- Detailed Food Category Analysis:
     - For the top 3 food categories with the highest microplastic content, analyze their individual trends over time (1990-2018). Are some increasing more rapidly than others?
     - Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1991) and latest (2018) years. Describe the shifts in contribution.
"""


"""
- Country-Specific Microplastic Profiles:
    - Select two countries with significantly different average total_ug_per_kg (one high, one low, from your beginner analysis).
    - For each selected country, visualize the breakdown of total_ug_per_kg by different food categories for the year 2018. Highlight the food categories contributing most to microplastic intake in these specific countries.
"""

"""
## My roadmap:
  We need to limit our data to year of 2018 and only two countries. First I make a new data frame that contains all the data for the year 2018.
  I decided to get the countries with the highest and lowest averages, which we have from the beginner's questions.
  I make two other data frames, by restricting df_2018 to those country rows that I need.
  Then I drop the columns that I don't need (year, country, total_ug_per_kg).
  I also need to sort the values, but I couldn't simply do it by sort_values(), because I need to sort the data by a column. But here, I have many columns (each food category is one column). So, I need to swap the columns and rows. I do it with melt(). Now I can sort my values. Since this setting won't be saved in the original data, I need to put it into another variable.
"""


def visualize_breakdown_for_highest_and_lowest_countries_in_a_specific_year(
    df, specific_year, highest_high_low_countries, lowest_high_low_countries
):
    # restricing data to the specific year
    df_specific_year = df[df["year"] == specific_year]

    # restricting the data to two countries with highest and lowest average consumption
    df_specific_year_high_country = df_specific_year[
        df_specific_year["country"] == highest_high_low_countries.index[0]
    ]
    df_specific_year_low_country = df_specific_year[
        df_specific_year["country"] == lowest_high_low_countries.index[-1]
    ]

    # dropping the unwanted columns
    df_foods_high_country = df_specific_year_high_country.drop(
        columns=["year", "country", "total_ug_per_kg"]
    )
    df_foods_low_country = df_specific_year_low_country.drop(
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
    # preparing x and y axis for the bar chart
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
    plt.title("Microplastic Breakdown for Greece (2018)")
    plt.xlabel("Food Category")
    plt.ylabel("Microplastics (µg/kg)")
    plt.tight_layout()
    plt.savefig("output/5_microplastic_breakdown_high_country")

    # plotting for the country with the lowest microplastic intake
    bar_colors_low = []

    for v in low_country_value:
        if v >= 100:
            bar_colors_low.append("tab:red")
        else:
            bar_colors_low.append("tab:blue")

    plt.figure(figsize=(12, 6))
    plt.bar(low_country_food_category, low_country_value, color=bar_colors_low)
    plt.xticks(rotation=90)
    plt.title("Microplastic Breakdown for Bangladesh (2018)")
    plt.xlabel("Food Category")
    plt.ylabel("Microplastics (µg/kg)")
    plt.tight_layout()
    plt.savefig("output/6_microplastic_breakdown_low_country")
    
    
    """ 
    -- Additional Analysis --
    I was thinking we could add one more perspective on the country-level results.
    Right now we look at total_ug_per_kg (the sum across categories), which tells us the overall exposure risk.
    But if we also compute the average per category and the spread between categories (e.g., standard deviation or share of the largest category),
    we can distinguish between two situations:
    Situation a) Countries where microplastic contamination is concentrated in just one or two categories (e.g., almost everything comes from fish).
    Situation b) Countries where contamination is more evenly spread across many categories (so the risk is systemic).

    This would give us a clearer picture of whether high totals are due to a single problematic food group or a general baseline contamination across the whole diet.
    """

    # Question: Is the contamination in each country coming from one (or a few) food categories, or is it widespread across categories?

    '''
    We will use three concentration metrics:
    1. Mean per category: the average contamination across food groups.
    2. Standard deviation across categories: higher std means big differences between categories, therefore more concentration.
    3. Max share: share of the biggest contributing category.
    '''

    food_categories = [
        col for col in df.columns if col not in ["country", "year", "total_ug_per_kg"]
    ]

    # calulating average microplastic content across all food categories for each country
    country_avgs = df.groupby("country")[food_categories].mean()

    # caluclating the concentration_metrics
    # setting the axis=1, so it does the calculations for each row (not column)
    concentration_metrics = pd.DataFrame({
        "mean_per_category": country_avgs.mean(axis=1),
        "std_per_category": country_avgs.std(axis=1),
        "max_share": country_avgs.max(axis=1) / country_avgs.sum(axis=1)
    })

    #sorting the results by max share and printing it
    concentration_metrics = concentration_metrics.sort_values("max_share", ascending=False)
    print("\n 10 Countries with most concentrated contamination: \n ", concentration_metrics.head(10))
    print("\n 10 Countries with most widespread contamination: \n", concentration_metrics.tail(10))

    '''
    Looking at the results, it seems like those countries in which a single food category has a large share of the total contamination, are African countries.
    I want to investigate this further. I use pycountry_convert library, to get the continent names for each country and group the data by the continents.
    '''
    # I reset the index so that I can work with the names of the countries
    concentration_metrics = concentration_metrics.reset_index()

    # I write a function that takes a country name and gives me back the continent
    # to be honest, I wasn't sure which functions from the library to use. so I had to look up that first I need the alpha2 country code(the official two-letter code for a country), and then from there I can get the continent code.
    def get_continent(country):
        # Some country names in my data don’t match perfectly with the library, so I have to use try/except and return None if it fails
        try:
            # First I convert the country name to a 2-letter code (like 'DE' for Germany).
            code = pc.country_name_to_country_alpha2(country)
            # Then I convert that code to a continent code (like 'EU' for Europe).
            return pc.country_alpha2_to_continent_code(code)
        except:
            return None

    concentration_metrics["continent"] = concentration_metrics["country"].apply(get_continent)
    continent_breakdown = concentration_metrics.groupby("continent")["max_share"].mean().sort_values(ascending=False)
    print('\n Average share of the most contaminated food category for each continent \n', continent_breakdown)

    """
    Now, I want to see which single category has the max share in my top 10 countries.
    I thought I can just loop through them one by one.
    """

    # putting top 10 most concentrated countries into a variable
    top10_countries = concentration_metrics.head(10)["country"]

    # I decided to make a dictionary, because I want to store multiple things for each country
    top10_biggest_contributors = {}

    for country in top10_countries:
        # I take the row for that country (all the categories with their values)
        country_data = country_avgs.loc[country]

        # I wasn’t sure how to find the category with the max value, at first I thought about sorting, but then I learned there is .idxmax() which directly gives the category name
        top_category = country_data.idxmax()

        # here I just get the actual value of that max contamination
        top_value = country_data.max()

        # and the sum across all categories (I need this to calculate the share)
        total_value = country_data.sum()

        share = top_value / total_value

        # I put the results into the dictionary under the country name
        # I wasn’t sure whether to use a list or dictionary here — I picked dictionary because I want to access results by country name later, not just by position
        # also rounded the share to make it cleaner
        top10_biggest_contributors[country] = {
            "top_category": top_category,
            "share": round(share, 3),
            "value": round(top_value, 2)
        }

    # I convert results to a dataframe for a better view
    top10_contributors_df = pd.DataFrame(top10_biggest_contributors).T
    print("\n Top contributors in top 10 most concentrated countries:\n")
    print(top10_contributors_df)

    '''
    The result is interesting. Refined grains is the dominant source in 9 out of 10 of the countries with most concentrated pollution.
    I want to check this across all countries. I will count how many times each category is the top contributor.
    '''

    # To find the top contributor for each country I again use idxmax() that returns the index for the maximum value in each column
    # By setting the axis to 1, it will do it for each row
    top_category_per_country = country_avgs.idxmax(axis=1)

    # Counting frequencies
    top_category_counts = top_category_per_country.value_counts()
    print("\n How often each category is the biggest contributor:\n", top_category_counts)

    #Plotting a bar chart: I found out I can work with .plot() and I don't have to put each column into a list (as I used to do when plotting with plt.bar())!
    plt.figure(figsize=(10, 6))
    top_category_counts.plot(kind="bar")
    plt.title("Most Frequent Top Contributors Across Countries")
    plt.ylabel("Number of countries")
    plt.xlabel("Food category")
    plt.tight_layout()
    plt.savefig("output/8_biggest_contributors_count")




"""
- Growth Rate Analysis:
    - Calculate the percentage increase in total_ug_per_kg from 1990 to 2018 for each country. Identify the top 5 countries with the highest growth rate in microplastic consumption.
    - Investigate which food categories are driving this growth in those top 5 countries.
"""


def analyze_growth_rate(
    df, start_year=None, end_year=2018, top_n_countries=5, top_n_food_categories=3
):
    # Determine earliest year per country if start_year not provided
    if start_year is None:
        first_year = (
            df.groupby("country")["year"].min().rename("first_year").reset_index()
        )
    else:
        first_year = pd.Series(
            start_year, index=df["country"].unique(), name="first_year"
        ).reset_index()
        first_year.columns = ["country", "first_year"]

    df_first = pd.merge(
        first_year,
        df,
        left_on=["country", "first_year"],
        right_on=["country", "year"],
        how="left",
    )
    df_first = df_first[["country", "first_year", "total_ug_per_kg"]].rename(
        columns={"first_year": "year", "total_ug_per_kg": "first_value"}
    )

    # Get last year per country (or use fixed end_year if specified)
    if end_year is None:
        last_year = (
            df.groupby("country")["year"].max().rename("last_year").reset_index()
        )
    else:
        last_year = pd.Series(
            end_year, index=df["country"].unique(), name="last_year"
        ).reset_index()
        last_year.columns = ["country", "last_year"]

    df_last = pd.merge(
        last_year,
        df,
        left_on=["country", "last_year"],
        right_on=["country", "year"],
        how="left",
    )
    df_last = df_last[["country", "last_year", "total_ug_per_kg"]].rename(
        columns={"last_year": "year", "total_ug_per_kg": "last_value"}
    )

    # Merge for growth calculation
    df_growth = pd.merge(df_first, df_last, on="country")
    df_growth["period_years"] = df_growth["year_y"] - df_growth["year_x"]

    # CAGR calculation with safety checks to avoid division by zero
    df_growth["growth_rate"] = np.where(
        (df_growth["first_value"] > 0) & (df_growth["period_years"] > 0),
        (df_growth["last_value"] / df_growth["first_value"])
        ** (1 / df_growth["period_years"])
        - 1,
        np.nan,
    )

    # Get top N countries by growth_rate
    top_growth = df_growth.sort_values("growth_rate", ascending=False).head(
        top_n_countries
    )
    top_countries = top_growth["country"].tolist()

    # Identify food columns (excluding country, year, total_ug_per_kg)
    food_categories = [
        col for col in df.columns if col not in ["country", "year", "total_ug_per_kg"]
    ]

    # Prepare results container
    results = []

    for country in top_countries:
        start_y = first_year.loc[first_year["country"] == country, "first_year"].values[
            0
        ]
        end_y = last_year.loc[last_year["country"] == country, "last_year"].values[0]
        years = end_y - start_y

        for food in food_categories:
            start_val = df.loc[
                (df["country"] == country) & (df["year"] == start_y), food
            ].values
            end_val = df.loc[
                (df["country"] == country) & (df["year"] == end_y), food
            ].values

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

            results.append(
                {
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
                }
            )

    df_growth_rates = pd.DataFrame(results)

    # Pivot for convenience: CAGR and slope percent per food category by country
    growth_pivot = df_growth_rates.pivot(
        index="country",
        columns="food_category",
        values=["CAGR", "slope_percent_per_year"],
    )

    # Extract top food categories by CAGR and slope percent per country
    top_drivers_cagr = (
        df_growth_rates.sort_values(["country", "CAGR"], ascending=[True, False])
        .groupby("country")
        .head(top_n_food_categories)
    )
    top_drivers_slope = (
        df_growth_rates.sort_values(
            ["country", "slope_percent_per_year"], ascending=[True, False]
        )
        .groupby("country")
        .head(top_n_food_categories)
    )

    return {
        "top_countries_growth": top_growth,
        "top_drivers_cagr": top_drivers_cagr,
        "top_drivers_slope": top_drivers_slope,
        "growth_pivot": growth_pivot,
    }


"""
- Correlation between Food Groups (Optional/Advanced):
    - Is there a correlation between microplastic content in different food groups? For example, do countries with high microplastic in fish also tend to have high microplastic in seafood or processed_foods? Use correlation matrices or scatter plots to explore.
"""


def get_correlation_regarding_a_column(
    df: pd.DataFrame, corr_check_method: str, corr_check_col: str
) -> None:
    # Get the correlation matrix
    df.corr

    # define a vairable with the correlation regardint numerics only.
    corr = df.corr(method=corr_check_method, min_periods=1, numeric_only=True)

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
    plt.savefig("output/7_intermediate_correlation_of_microplastics.png")

    return None


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

    print("\n")
    plot_food_category_trend(df, "total_milk")

    # - Detailed Food Category Analysis:
    #     - For the top 3 food categories with the highest microplastic content, analyze their individual trends over time (1990-2018). Are some increasing more rapidly than others?
    #     - Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1991) and latest (2018) years. Describe the shifts in contribution.

    # Find out the total per year of all countries together for the top 3 food categories
    # Extract just the column names from the top 3 tuples
    mean_list = calculate_top_n_contaminated_categories(df, 3, 2, -1)
    top_3_columns = [category for category, avg in mean_list[:3]]

    total_highest = df.groupby("year")[top_3_columns].sum()

    # Plot a line chart to visualize the trends of each category
    ax = total_highest.plot(marker="o", figsize=(10, 6))

    plt.title("Microplastic Content in 3 Food Categories with The Highest Contamination (1990-2018)")
    plt.xlabel("Year")
    plt.ylabel("Total µg/kg")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("output/4_intermediate_food_trends.png")

    # Create a new dictionary for the results
    results = {}

    # Use slope to calculate the increase
    for cat in top_3_columns[0:3]:
        y = total_highest[cat].values
        x = total_highest.index.values
        slope = np.polyfit(x, y, 1)[0]
        results[cat] = slope

    # Make an order from fastest to slowest increase
    sorted_results = dict(
        sorted(results.items(), key=lambda item: item[1], reverse=True)
    )
    for cat, slope in sorted_results.items():
        print(f"{cat}: {slope:.2f} µg/kg per year")

    print()

    # Print the category with the fastest increase
    fastest = max(results, key=results.get)
    print(f"Fastest increase: {fastest} ({results[fastest]:.2f} µg/kg per year)")

    # Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1990) and latest (2018) years

    # Filter the food columns (first 2 columns and last column are no food)
    food_columns = df.columns[2:-1]

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
    print("\n The share of each food category in the total microplastic contamination: \n", p_compare)

    # Describe the shifts in contribution / changes
    change_dec = (
        (percentage_dec.loc[2018] - percentage_dec.loc[1990]) / percentage_dec.loc[1990]
    ) * 100
    change_p = change_dec.map(lambda x: f"{x:.2f}%")

    # Sort in decreasing order
    change_dec_sorted = change_dec.sort_values(ascending=False)
    change_p_sorted = change_dec_sorted.map(lambda x: f"{x:.2f}%")
    print('\n The growth rate in contribution share from 1990 to 2018: \n ', change_p_sorted)

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


    '''
    Additional Analysis on this question:
    1) rank of which categories changed between 1990 and 2018?
    2) visualization of shares with a stacked area chart
    3) calculating CAGR for each category (instead of slopes)
    '''

    ## 1) Rank shift analysis

    # Rank food categories by contribution in 1990 and 2018
    rank_1990 = percentage_dec.loc[1990].rank(ascending=False)
    rank_2018 = percentage_dec.loc[2018].rank(ascending=False)

    rank_shift = (rank_1990 - rank_2018).sort_values()

    print("\n Rank shifts (Positive numbers show that the category has gained a higher share of the total, and vice versa.): \n\n", rank_shift)

    ## 2) Stacked area chart for shares over time

    # I want to see how each food category's share changes over time.
    # First I group the data by year and sum up the values for each category
    shares_over_time = df.groupby("year")[food_columns].sum()

    # I realized these are absolute totals, and I want percentages. So, I divide each row by the row sum (total across all food categories for that year).
    shares_over_time = shares_over_time.div(shares_over_time.sum(axis=1), axis=0) * 100

    # Now I can make a stacked area chart. I tried line plot first, but it looked messy since all categories overlapped.
    shares_over_time.plot.area(figsize=(12, 6), alpha=0.7)
    plt.title("Evolution of Food Category Shares (1990–2018)")
    plt.ylabel("Share of Total (%)")
    plt.xlabel("Year")
    plt.tight_layout()
    plt.savefig("output/food_category_shares_over_time.png")

    ## 3) Calculating CAGR

    cagr_results = {}
    for cat in food_columns:
        first = total_cat_year.loc[1990, cat]
        last = total_cat_year.loc[2018, cat]
        years = 2018 - 1990
        cagr = ((last / first) ** (1/years) - 1) * 100
        cagr_results[cat] = cagr

    cagr_sorted = pd.Series(cagr_results).sort_values(ascending=False)
    print("\n\n Compound Annual Growth Rate (CAGR) 1990–2018 (%):\n\n", cagr_sorted)

    # Making a nice summary of all data for better viewing
    summary = pd.DataFrame({
        "1990 Share": percentage_dec.loc[1990],
        "2018 Share": percentage_dec.loc[2018],
        "Rank 1990": rank_1990,
        "Rank 2018": rank_2018,
        "Rank Change": rank_1990 - rank_2018,
        "CAGR %": pd.Series(cagr_results)
    }).sort_values("CAGR %", ascending=False)

    print("\n\n Which categories are overtaking the other?\n\n ", summary)


    # for the question I already set the parameters, is changeable however to anything one wants.
    highest_high_low_countries, lowest_high_low_countries = (
        highest_lowest_high_low_countries(df, "total_ug_per_kg", "mean", 5)
    )

    # here for the wanted effect I already set the parameters, is changeable however to anything one wants.
    get_correlation_regarding_a_column(df, "pearson", "total_ug_per_kg")

    # calculate_top_n_contaminated_categories(df, n, start_food_col, end_food_col)
    calculate_top_n_contaminated_categories(df, 3, 2, -1)

    # plot_top_n_contaminated_categories(df, n, mean_list)
    plot_top_n_contaminated_categories(df, 10, mean_list)

    # visualize_breakdown_for_highest_and_lowest_countries_in_a_specific_year(df, specific_year, highest_high_low_countries, lowest_high_low_countries)
    visualize_breakdown_for_highest_and_lowest_countries_in_a_specific_year(
        df, 2018, highest_high_low_countries, lowest_high_low_countries
    )


if __name__ == "__main__":
    main()
