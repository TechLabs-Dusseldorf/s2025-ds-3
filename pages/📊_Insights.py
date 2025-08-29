import streamlit as st
import pandas as pd
import plotly.express as px
import io


st.set_page_config(
    page_title="Insights", page_icon="🔎", layout="centered"
)

st.title("📊 Key Insights")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
This page presents our main insights from the dataset provided by the <strong>PurePlate Initiative</strong>.  
We structured our findings around key questions we had during the analysis.
</p>
""", unsafe_allow_html=True)

# ---------------------------
# Helper functions
# ---------------------------
def insight_section(title, icon, text):
    st.markdown(f"""
    <div style="
        background-color:#fffafa; padding:20px; border-radius:12px; 
        box-shadow:0 4px 8px rgba(0,0,0,0.05); margin-bottom:30px;
        font-family: 'Arial', sans-serif;">
        <h2 style="margin-top:0;">{icon} {title}</h2>
        <p style="color:#2e3d49; font-size:16px; line-height:1.6;">{text}</p>
    </div>
    """, unsafe_allow_html=True)

def display_chart(chart_path):
    st.image(chart_path)

# Function to load & inspect
@st.cache_data
def load_and_inspect_data(filepath):
    df = pd.read_csv(filepath)

    st.subheader("➡️ A first look at the dataset")
    st.dataframe(df.head())

    st.subheader("➡️ Data types and memory usage")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.code(s)

    return df

# ---------------------------
# Section 1: Data Loading
# ---------------------------
insight_section(
    "Data Loading and Initial Exploration",
    "📂",
    "We began by loading the dataset, inspecting its structure, and performing basic cleaning steps. Since the dataset did not include any null or NaN values, no targeted preprocessing measures were needed."
)

# Replace with actual df.head()
load_and_inspect_data("processed_microplastics.csv")

# ---------------------------
# Section 2: Overall Trends
# ---------------------------
insight_section(
    "Overall Trends in Microplastic Consumption",
    "📉",
    "We wanted to understand the big picture: what does global microplastic exposure look like over time?"
)

st.subheader("➡️ Overall average consumption across all countries and years")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
As a general trend, microplastic contamination in our food is visibly rising, the overall average consumption across all countries and years being <strong>1600.6 µg/kg</strong>.
</p>
""", unsafe_allow_html=True)

display_chart("output/1_total_ug_kg_year.png")

# ---------------------------
# Section 3: High-Risk Food Categories
# ---------------------------
insight_section(
    "High-Risk Food Categories",
    "🥫",
    "Which foods contribute the most to microplastic intake?"
)

st.subheader("➡️ Top 3 food categories by microplastic content")
display_chart("output/2_average_consumption_top_n_food_categories.png")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
Here, we took a closer look at the three categories with the highest microplastic concentrations.  
Their trends over time are summarized below:
</p>

<ul style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
  <li><strong>Refined grains</strong> (220.60 µg/kg per year): Steady from 1990 to 2005, followed by a significant upward jump.</li>
  <li><strong>Milk</strong> (-17.32 µg/kg per year): Slowly rising until 2005, then a sharp drop. Recovery starts after 2010, but levels in 2018 remain lower than before the 2005 drop (hence the negative growth rate).</li>
  <li><strong>Non-starchy vegetables</strong> (351.41 µg/kg per year): Continuous fast growth across the whole period, showing no signs of improvement. This is the fastest-increasing category among the three.</li>
</ul>
""", unsafe_allow_html=True)

st.subheader("➡️ Growth speed for top 3 food categories")
display_chart("output/4_analyze_microplastic_trends.png")
st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
Non-starchy vegetables exhibit the fastest increase in microplastic content (351.41 µg/kg per year), followed by refined grains (220.60 µg/kg per year). Milk, in contrast, is decreasing slightly (-17.32 µg/kg per year).
</p>
""", unsafe_allow_html=True)

st.subheader("➡️ Changes in contribution of food categories (1990 vs 2018)")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
">
Below, we compare how different food categories contributed to total microplastic intake in 1990 and 2018.
The percentages indicate each category's share of total μg/kg consumption.
</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("**1990 Contribution (%)**")
    st.table({
        "Food Category": ["cheese","yoghurt","total_milk","fruits","refined_grains",
                          "whole_grains","nuts_and_seeds","total_processed_meats",
                          "unprocessed_red_meats","fish","shellfish","eggs",
                          "total_salt","added_sugars","non-starchy_vegetables",
                          "potatoes","other_starchy_vegetables","beans_and_legumes"],
        "Percentage": ["0.38%","3.55%","17.18%","12.47%","20.36%",
                       "4.89%","0.70%","2.65%","5.43%","2.38%","0.46%",
                       "0.99%","0.45%","5.03%","12.96%","4.89%","4.06%","1.19%"]
    })

with col2:
    st.markdown("**2018 Contribution (%)**")
    st.table({
        "Food Category": ["cheese","yoghurt","total_milk","fruits","refined_grains",
                          "whole_grains","nuts_and_seeds","total_processed_meats",
                          "unprocessed_red_meats","fish","shellfish","eggs",
                          "total_salt","added_sugars","non-starchy_vegetables",
                          "potatoes","other_starchy_vegetables","beans_and_legumes"],
        "Percentage": ["0.42%","3.32%","14.25%","12.41%","19.03%",
                       "4.67%","0.82%","2.74%","5.88%","2.60%","0.47%",
                       "1.23%","0.41%","6.02%","15.58%","4.97%","3.97%","1.19%"]
    })

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
">
Some notable shifts between 1990 and 2018:

<ul style="margin-left:20px;">
    <li><strong>Eggs</strong> increased substantially (+24.6%), becoming a more prominent source of microplastics.</li>
    <li><strong>Non-starchy vegetables</strong> also grew (+20.2%), reflecting the rising exposure from plant-based foods.</li>
    <li><strong>Added sugars</strong> and <strong>nuts & seeds</strong> showed moderate increases (+19.8% and +17.9%, respectively).</li>
    <li>In contrast, <strong>milk</strong> (-17.1%), <strong>total salt</strong> (-8.7%), and <strong>refined grains</strong> (-6.5%) decreased in relative contribution over the period.</li>
</ul>

These shifts highlight that while some traditional staples contribute less, newer or processed food categories are becoming more significant sources of microplastics.
</p>
""", unsafe_allow_html=True)

st.subheader("➡️ Changes in Main Contributing Categories Over Time")
display_chart("output/9_food_category_shares_over_time.png")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
Have the main contributing food categories changed over time, and could other foods pose greater risks in the future?
</p>

<ul style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
    <li><strong>Refined grains</strong> and <strong>milk</strong> remain the top contributors but have lost relative share since 1990.</li>
    <li><strong>Milk</strong> dropped from <strong>17.18%</strong> (1990) to <strong>13.24%</strong> (2018), a decline of <strong>-17.10%</strong>, the largest drop among all categories.</li>
    <li><strong>Refined grains</strong> fell from <strong>20.36%</strong> to <strong>19.03%</strong> (a -6.53% decline).</li>
    <li>Other categories, whose absolute contributions are still lower, are gaining a larger share, but the shifts are relatively minor.</li>
    <li>Analyzing rank shifts reveals that the relative contributions of most food categories have remained largely unchanged between 1990 and 2018.</li>
    <li>This stability suggests that contamination patterns are structurally persistent, and interventions so far have not significantly changed which foods dominate contamination risks.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">
The table below shows how the share of different food categories has shifted from 1990 to 2018. 
Columns show the percentage share in each year, the rank in both years, the rank change, and the compound annual growth rate (CAGR %).
</p>

<table style="
    font-family: 'Arial', sans-serif; 
    border-collapse: collapse; 
    width: 100%; 
    margin-bottom: 20px;">
    <tr style="background-color:#f2f2f2;">
        <th style="border: 1px solid #ddd; padding: 8px;">Food Category</th>
        <th style="border: 1px solid #ddd; padding: 8px;">1990 Share</th>
        <th style="border: 1px solid #ddd; padding: 8px;">2018 Share</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Rank 1990</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Rank 2018</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Rank Change</th>
        <th style="border: 1px solid #ddd; padding: 8px;">CAGR %</th>
    </tr>
    <tr><td>eggs</td><td>0.99%</td><td>1.23%</td><td>14</td><td>13</td><td>+1</td><td>1.57</td></tr>
    <tr><td>non-starchy_vegetables</td><td>12.96%</td><td>15.58%</td><td>3</td><td>2</td><td>+1</td><td>1.44</td></tr>
    <tr><td>added_sugars</td><td>5.03%</td><td>6.02%</td><td>6</td><td>5</td><td>+1</td><td>1.43</td></tr>
    <tr><td>nuts_and_seeds</td><td>0.70%</td><td>0.82%</td><td>15</td><td>15</td><td>0</td><td>1.37</td></tr>
    <tr><td>cheese</td><td>0.38%</td><td>0.42%</td><td>18</td><td>17</td><td>+1</td><td>1.13</td></tr>
    <tr><td>fish</td><td>2.38%</td><td>2.60%</td><td>12</td><td>12</td><td>0</td><td>1.10</td></tr>
    <tr><td>unprocessed_red_meats</td><td>5.43%</td><td>5.88%</td><td>5</td><td>6</td><td>-1</td><td>1.06</td></tr>
    <tr><td>total_processed_meats</td><td>2.65%</td><td>2.74%</td><td>11</td><td>11</td><td>0</td><td>0.91</td></tr>
    <tr><td>shellfish</td><td>0.46%</td><td>0.47%</td><td>16</td><td>16</td><td>0</td><td>0.87</td></tr>
    <tr><td>potatoes</td><td>4.89%</td><td>4.97%</td><td>8</td><td>7</td><td>+1</td><td>0.83</td></tr>
    <tr><td>beans_and_legumes</td><td>1.19%</td><td>1.19%</td><td>13</td><td>14</td><td>-1</td><td>0.76</td></tr>
    <tr><td>fruits</td><td>12.47%</td><td>12.41%</td><td>4</td><td>4</td><td>0</td><td>0.76</td></tr>
    <tr><td>other_starchy_vegetables</td><td>4.06%</td><td>3.97%</td><td>9</td><td>9</td><td>0</td><td>0.70</td></tr>
    <tr><td>whole_grains</td><td>4.89%</td><td>4.67%</td><td>7</td><td>8</td><td>-1</td><td>0.61</td></tr>
    <tr><td>yoghurt</td><td>3.55%</td><td>3.32%</td><td>10</td><td>10</td><td>0</td><td>0.54</td></tr>
    <tr><td>refined_grains</td><td>20.36%</td><td>19.03%</td><td>1</td><td>1</td><td>0</td><td>0.53</td></tr>
    <tr><td>total_salt</td><td>0.45%</td><td>0.41%</td><td>17</td><td>18</td><td>-1</td><td>0.44</td></tr>
    <tr><td>total_milk</td><td>17.18%</td><td>14.25%</td><td>2</td><td>3</td><td>-1</td><td>0.10</td></tr>
</table>

<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
">
This table highlights the few categories that have moved up in rank (eggs, non-starchy vegetables, added sugars, cheese, potatoes), while others like milk and refined grains lost relative share. Overall, the system is largely stable, showing that contamination patterns are persistent over time.
</p>
""", unsafe_allow_html=True)

# ---------------------------
# Section 4: Geographic Variations
# ---------------------------
insight_section(
    "Geographical Variations in Microplastic Intake",
    "🌍",
    "Microplastic exposure differs widely across countries and regions."
)

#st.write("➡️ 5 countries with highest and lowest average intake")
#col1, col2 = st.columns(2)
#with col1: placeholder_table("Top 5 countries")
#with col2: placeholder_table("Lowest 5 countries")

#placeholder_chart("World map of average intake by country")

#st.markdown("#### Country-Specific Profiles (2018)")
#col1, col2 = st.columns(2)
#with col1: placeholder_chart("Figure #5: Country A breakdown (2018)")
#with col2: placeholder_chart("Figure #6: Country B breakdown (2018)")

#st.markdown("#### Growth Rate Analysis")
#placeholder_table("Top 5 countries with highest growth rate (1990–2018)")
#placeholder_table("Food categories driving growth")

#st.markdown("#### Concentration vs Widespread Contamination")
#col1, col2 = st.columns(2)
#with col1: placeholder_table("10 Countries with most concentrated contamination")
#with col2: placeholder_table("10 Countries with most widespread contamination")
#placeholder_table("Average share of most contaminated food category per continent")
#placeholder_chart("Figure #8: Contamination distribution across categories")

# ---------------------------
# Section 5: Correlation (Optional)
# ---------------------------
insight_section(
    "Correlation Between Food Groups (Optional/Advanced)",
    "🧩",
    "Do certain food categories co-occur in their contamination levels? This analysis explores correlations."
)
#placeholder_chart("Correlation heatmap / scatter matrix")

# ---------------------------
# Closing Callout
# ---------------------------
st.markdown("""
<hr style="margin:40px 0;">
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
">
Together, these findings provide a comprehensive overview of the presence of 
<strong>microplastics in our food system</strong>. They highlight urgent challenges 
and point to areas where further research is needed. One promising avenue for future 
investigation is the application of <strong>machine learning algorithms 🤖</strong> 
to forecast trends, which could help predict how microplastic contamination might 
evolve over time and inform more proactive interventions.
</p>
""", unsafe_allow_html=True)