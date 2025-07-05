# Welcome Group3 to your project phase

Data-Link: https://www.kaggle.com/datasets/jayeshrmohanani/dataset-for-microplastic-consumption-in-food-items/data?select=processed_microplastics.csv

## The scenario: Processed Microplastics
You are now working with the PurePlate Initiative, a global non-profit advocacy group dedicated to promoting food safety and raising awareness about emerging contaminants in the human diet. The PurePlate Initiative is particularly concerned about the increasing presence of microplastics in our food supply and its potential long-term health implications.
They have acquired a unique dataset on estimated microplastic consumption and need your team to conduct a thorough analysis. The goal is to identify trends, pinpoint high-risk food categories, and understand geographical variations in microplastic intake. Your findings will be crucial for informing public health campaigns, influencing dietary guidelines, and advocating for stricter regulations on plastic production and waste management.


## The task
Your task is to leverage this dataset to provide the PurePlate Initiative with data-driven insights on microplastic consumption in various food items across different countries and over time. Your analysis will form the basis of their next major report and public awareness efforts.

- Document all your steps and thoughts, so the mentors can follow your process
- Prepare a nice README.md for your project
- Think about how you can present your results for different target groups

## Some guidance (optional, if needed)
Your analysis can address the following questions, categorized by complexity.
If you want to add or do others, feel free to do so. 
If you can find additional data that suits your original dataset, feel free to implement it.

### Beginner Questions
- Data Loading and Initial Exploration:
    - Load the dataset into a pandas DataFrame.
    - Display the first 5 rows and check the data types of all columns.
    - Identify and handle any missing values.
    - List all unique Country values in the dataset.
- Overall Trends in Microplastic Consumption:
    - What is the average total_ug_per_kg across all countries and years in the dataset?
    - How has the global average total_ug_per_kg changed over the years (1990-2018)? Visualize this trend.
- Top Food Contributors:
    - Which 3 food categories (product columns, e.g., fish, poultry, vegetables) show the highest average microplastic consumption (μg/kg) across all countries and years?
    - Visualize the average microplastic content for the top 10 food categories.
- Country-Level Totals:
    - Which 5 countries have the highest average total_ug_per_kg over the entire period (1990-2018)?
    - Which 5 countries have the lowest average total_ug_per_kg?
- Initial Time-Series for a Food Category:
    - Choose one of the top 3 food categories identified in question 3. How has the microplastic content in this specific food category changed over time (1990-2018) globally? Visualize this trend.
### Intermediate Questions
- Detailed Food Category Analysis:
    - For the top 3 food categories with the highest microplastic content, analyze their individual trends over time (1990-2018). Are some increasing more rapidly than others?
    - Compare the contribution of different food categories to the total_ug_per_kg in the earliest (1990) and latest (2018) years. Describe the shifts in contribution.
- Country-Specific Microplastic Profiles:
    - Select two countries with significantly different average total_ug_per_kg (one high, one low, from your beginner analysis).
    - For each selected country, visualize the breakdown of total_ug_per_kg by different food categories for the year 2018. Highlight the food categories contributing most to microplastic intake in these specific countries.
- Growth Rate Analysis:
    - Calculate the percentage increase in total_ug_per_kg from 1990 to 2018 for each country. Identify the top 5 countries with the highest growth rate in microplastic consumption.
    - Investigate which food categories are driving this growth in those top 5 countries.
- Correlation between Food Groups (Optional/Advanced):
    - Is there a correlation between microplastic content in different food groups? For example, do countries with high microplastic in fish also tend to have high microplastic in seafood or processed_foods? Use correlation matrices or scatter plots to explore.
### Public Health Implications & Recommendations (Qualitative):
- Based on your findings, what are 2-3 key insights you would present to the PurePlate Initiative regarding microplastic consumption?
- Propose potential policy recommendations or public awareness strategies that could help reduce human exposure to microplastics through diet, citing evidence from your analysis.

Remember to provide clear visualizations and concise explanations for all your findings. Your analysis will contribute directly to a vital public health discussion!
