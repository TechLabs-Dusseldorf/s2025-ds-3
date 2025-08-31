import streamlit as st
import pandas as pd
import plotly.express as px
import pycountry
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

insight_section(
    "Data Loading and Initial Exploration",
    "📂",
    "We began by loading the dataset, inspecting its structure, and performing basic cleaning steps. Since the dataset did not include any null or NaN values, no targeted preprocessing measures were needed."
)

# Replace with actual df.head()
load_and_inspect_data("processed_microplastics.csv")

insight_section(
    "Overall Trends in Microplastic Consumption",
    "📉",
    "We wanted to understand the big picture: what does global microplastic exposure look like over time?"
)

st.subheader("➡️ Rising Trend of Global Food Microplastic Intake")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
Microplastic contamination in our food is visibly rising, the overall average consumption across all countries and years being <strong>1600.6 µg/kg</strong>.
</p>
""", unsafe_allow_html=True)

display_chart("output/1_total_ug_kg_year.png")

insight_section(
    "High-Risk Food Categories",
    "🥫",
    "Which foods contribute the most to microplastic intake?"
)

st.subheader("➡️ Refined Grains, Milk, and Vegetables Dominate Global Microplastic Intake")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
Across all countries and years, these three categories show the highest average contamination levels (μg/kg)</strong>.
</p>
""", unsafe_allow_html=True)

display_chart("output/2_average_consumption_top_n_food_categories.png")

st.subheader("➡️ How the Top Three Categories Have Evolved")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
The three biggest contributors tell three very different stories of risk.
</p>

<ul style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
  <li><strong>Refined grains</strong> looked stable at first, but after 2005 contamination spiked and has stayed dangerously high ever since.</li>
  <li><strong>Milk</strong> rose for years, then dropped sharply around 2005. Even with a partial rebound, today’s levels remain lower than before, making milk the only one moving in a less alarming direction.</li>
  <li><strong>Non-starchy vegetables</strong> are the most concerning: contamination has climbed relentlessly across the whole period, with no sign of slowing down.</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 26px;
">
Overall, non-starchy vegetables exhibit the fastest increase in microplastic content (351.41 µg/kg per year), followed by refined grains (220.60 µg/kg per year). Milk, in contrast, is decreasing slightly (-17.32 µg/kg per year).
</p>
""", unsafe_allow_html=True)

display_chart("output/4_analyze_microplastic_trends.png")

st.subheader("➡️ The Usual Suspects Haven’t Changed")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
">
When we compare how different food categories contributed to total microplastic intake in 1990 and 2018, at first glance, there seems to be a shift in the story. Two of the three categories with the highest average contamination (refined grains and milk) have actually lost share since 1990.
<ul style="
    margin-left:20px; 
    font-size: 17px; 
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    line-height: 1.7;
">
    <li><strong>Milk</strong> fell from 17.18% to 13.24%, the steepest drop of any category (−17.1%).</li>
    <li><strong>Refined grains</strong> slipped from 20.36% to 19.03% (−6.5%).</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
">
This decline might suggest that other foods are catching up and could become bigger threats in the future. But when we dig deeper, the picture turns out to be different. Rankings across food categories have barely changed in these years.
</p>
            
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
In other words, while shares have shifted slightly, the hierarchy of contamination is remarkably stable and persistent. The same foods that dominated three decades ago still dominate today. <strong>This stability suggests that contamination patterns are structurally persistent, and interventions so far have not significantly changed which foods dominate contamination risks</strong>.

</p>
""", unsafe_allow_html=True)

display_chart("output/9_food_category_shares_over_time.png")

insight_section(
    "Geographical Variations in Microplastic Intake",
    "🌍",
    "Microplastic exposure differs widely across countries and regions."
)

st.subheader("➡️ Record setters in average consumption")

## World map for countries with the highest and lowest average microplastic contamination

# Top 10 highest average consumption
top_10 = [
    "Greece", "Montenegro", "Dominica", "Barbados", "Albania",
    "Bosnia And Herzegovina", "Turkey", "United States",
    "Ukraine", "Netherlands"
]

# Bottom 10 lowest average consumption
bottom_10 = [
    "Djibouti", "Myanmar", "Cambodia", "Zimbabwe", "Ethiopia",
    "The Gambia", "Guinea-Bissau", "Burkina Faso", "Chad", "Bangladesh"
]

# All recognized country names from pycountry
all_countries = [country.name for country in pycountry.countries]

# Create dataframe
df = pd.DataFrame({"country": all_countries})

# Add highlight categories
def classify_country(x):
    if x in top_10:
        return "High (Top 10)"
    elif x in bottom_10:
        return "Low (Bottom 10)"
    else:
        return "Other"

df["highlight"] = df["country"].apply(classify_country)

# Color mapping: grey = others, red = high, blue = low
color_map = {
    "Other": "#eeeeee",
    "High (Top 10)": "#FF6B6B",
    "Low (Bottom 10)": "#4C9AFF"
}

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="highlight",
    hover_name="country",
    color_discrete_map=color_map
)

fig.update_layout(
    legend_title_text="Microplastic Level",
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)

fig.update_traces(
    hovertemplate="%{location}<extra></extra>"
)

fig.update_geos(projection_type="natural earth", fitbounds="locations", visible=False)

st.plotly_chart(fig, use_container_width=True, height=600)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<p style="text-align:center; font-size:16px; font-weight:bold;">5 Countries with Lowest Average Consumption</p>', unsafe_allow_html=True)
    st.markdown("""
    <table style="font-family: Arial, sans-serif; border-collapse: collapse; width: 100%;">
        <tr style="background-color:#f2f2f2;">
            <th style="border: 1px solid #ddd; padding: 8px;">Country</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Average Consumption</th>
        </tr>
        <tr><td>The Gambia</td><td>746.80</td></tr>
        <tr><td>Guinea-Bissau</td><td>738.99</td></tr>
        <tr><td>Burkina Faso</td><td>726.80</td></tr>
        <tr><td>Chad</td><td>717.14</td></tr>
        <tr><td>Bangladesh</td><td>634.60</td></tr>
    </table>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<p style="text-align:center; font-size:16px; font-weight:bold;">5 Countries with Highest Average Consumption</p>', unsafe_allow_html=True)
    st.markdown("""
    <table style="font-family: Arial, sans-serif; border-collapse: collapse; width: 100%;">
        <tr style="background-color:#f2f2f2;">
            <th style="border: 1px solid #ddd; padding: 8px;">Country</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Average Consumption</th>
        </tr>
        <tr><td>Greece</td><td>2844.98</td></tr>
        <tr><td>Montenegro</td><td>2601.90</td></tr>
        <tr><td>Dominica</td><td>2584.91</td></tr>
        <tr><td>Barbados</td><td>2504.98</td></tr>
        <tr><td>Albania</td><td>2454.38</td></tr>
    </table>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## Geographical Patterns and Possible Explanations")
st.markdown("""
<div style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">
<p>When comparing countries with the highest and lowest average microplastic contamination, certain patterns emerge that may point to underlying causes.</p>

<p><strong>1. Marine Geography</strong><br>
Many of the highest-consuming countries are located around <strong>semi-enclosed or enclosed seas</strong> such as the Mediterranean, Black Sea, and Caribbean. These waters have limited circulation, which may allow plastics to accumulate more than in open oceans.<br>
In contrast, several of the lowest-consuming countries are either <strong>landlocked</strong> (e.g., Chad, Burkina Faso, Ethiopia) or situated on coastlines linked to <strong>more open seas</strong> (e.g., Bay of Bengal, Gulf of Thailand), where pollutants may disperse more widely.</p>

<p><strong>2. Industrialization and Trade</strong><br>
Industrial and highly connected economies (e.g., the Netherlands, the United States, and Turkey) appear among the high-consumption group. This could reflect greater levels of plastic production, waste generation, and shipping activity, which are known sources of microplastics.<br>
Many of the countries with the lowest plastic consumption are <strong>less industrialized</strong> and generate less plastic waste overall, which may contribute to lower contamination levels.</p>

<p><strong>3. Food Packaging</strong><br>
In lower-income or less industrialized countries (e.g., Chad, Burkina Faso), foods are often sold fresh in markets with minimal plastic packaging, thereby reducing exposure to packaging sources.</p>
</div>
""", unsafe_allow_html=True)

insight_section(
    "Country-Specific Microplastic Profiles",
    "🧩",
    "Do certain food categories co-occur in their contamination levels? This analysis explores correlations."
)

st.markdown("""
<div style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">

<p>Let’s have a look at the differences in top contributors between the countries with the highest and lowest average microplastic consumption (μg/kg), which are <strong>Greece</strong> and <strong>Bangladesh</strong>, respectively.</p>

<p><strong>Greece (highest average consumption):</strong><br>
- Seven food categories contain more than 100 μg/kg of microplastics.<br>
- 9 out of Greece’s top 10 contaminated categories are also among the global top 10.<br>
- Interestingly, refined grains—globally the most contaminated—rank only seventh in Greece.<br>
- The standout issue is milk, with contamination exceeding 600 μg/kg, making it the most problematic category.</p>
</div>
""", unsafe_allow_html=True)

display_chart("output/5_microplastic_breakdown_high_country.png")

st.markdown("""
<div style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">
<p><strong>Bangladesh (lowest average consumption):</strong><br>
- Refined grains are the most contaminated category (consistent with the global pattern), with levels above 300 μg/kg.<br>
- Potatoes follow, but their contamination is almost half that of refined grains.</p>
</div>
""", unsafe_allow_html=True)

display_chart("output/6_microplastic_breakdown_low_country.png")

insight_section(
    "Countries with the Fastest Growth in Microplastic Consumption",
    "📈",
    "Calculating the Compound Annual Growth Rate, we were able to find out more about the countries with the fastest growth in microplastic consumption."
)

st.markdown("""
<table style="
    font-family: 'Arial', sans-serif;
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 20px;
">
    <tr style="background-color:#f2f2f2;">
        <th style="border: 1px solid #ddd; padding: 8px;">Country</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Starting Year</th>
        <th style="border: 1px solid #ddd; padding: 8px;">1990 Value (μg/kg)</th>
        <th style="border: 1px solid #ddd; padding: 8px;">2018 Value (μg/kg)</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Period (Years)</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Growth Rate</th>
    </tr>
    <tr><td>Croatia</td><td>2010</td><td>1861.64</td><td>2582.07</td><td>8</td><td>4.17%</td></tr>
    <tr><td>Laos</td><td>1990</td><td>713.83</td><td>1923.90</td><td>28</td><td>3.60%</td></tr>
    <tr><td>Belgium</td><td>2010</td><td>1734.37</td><td>2280.74</td><td>8</td><td>3.48%</td></tr>
    <tr><td>Myanmar</td><td>1990</td><td>493.48</td><td>1232.89</td><td>28</td><td>3.32%</td></tr>
    <tr><td>Vietnam</td><td>1990</td><td>639.51</td><td>1449.62</td><td>28</td><td>2.97%</td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
">
The table above highlights countries experiencing the fastest growth in microplastic consumption from 1990 to 2018. To understand what drives these trends, we examined the top food contributors in each high-growth country.
<ul style="
    margin-left:20px; 
    font-size: 17px; 
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    line-height: 1.7;
">
    <li>In <strong>Belgium</strong>, <strong>other starchy vegetables</strong> (CAGR 16.95%) and <strong>milk</strong> (CAGR 15.29%) were the largest contributors, with <strong>fruits</strong> also playing a role.</li>
    <li><strong>Croatia</strong> saw growth mainly in <strong>non-starchy vegetables</strong> (CAGR 18.83%), followed by <strong>processed and unprocessed red meats</strong>.</li>
    <li><strong>Laos</strong> experienced rises in <strong>added sugars</strong> (CAGR 10.97%) and <strong>non-starchy vegetables</strong> (CAGR 10.12%).</li>
    <li><strong>Myanmar</strong> growth was led by <strong>processed and red meats</strong> along with <strong>eggs</strong> (all ~9.3%).</li>
    <li><strong>Vietnam</strong> increases came mainly from <strong>nuts and seeds</strong>, <strong>shellfish</strong>, and <strong>cheese</strong> (CAGR 7–9%).</li>
</ul>
This shows that rapid microplastic growth is concentrated in specific high-consumption items rather than evenly across all foods.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<table style="
    font-family: 'Arial', sans-serif;
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 20px;
">
    <tr style="background-color:#f2f2f2;">
        <th style="border: 1px solid #ddd; padding: 8px;">Country</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Food Category</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Start Year</th>
        <th style="border: 1px solid #ddd; padding: 8px;">End Year</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Start Value (μg/kg)</th>
        <th style="border: 1px solid #ddd; padding: 8px;">End Value (μg/kg)</th>
        <th style="border: 1px solid #ddd; padding: 8px;">Period (Years)</th>
        <th style="border: 1px solid #ddd; padding: 8px;">CAGR</th>
    </tr>
    <tr><td>Belgium</td><td>Other Starchy Vegetables</td><td>2010</td><td>2018</td><td>0.99</td><td>3.45</td><td>8</td><td>16.95%</td></tr>
    <tr><td>Belgium</td><td>Milk</td><td>2010</td><td>2018</td><td>161.73</td><td>504.71</td><td>8</td><td>15.29%</td></tr>
    <tr><td>Belgium</td><td>Fruits</td><td>2010</td><td>2018</td><td>155.18</td><td>335.40</td><td>8</td><td>10.11%</td></tr>
    <tr><td>Croatia</td><td>Non-Starchy Vegetables</td><td>2010</td><td>2018</td><td>210.14</td><td>835.42</td><td>8</td><td>18.83%</td></tr>
    <tr><td>Croatia</td><td>Processed Meats</td><td>2010</td><td>2018</td><td>54.05</td><td>76.23</td><td>8</td><td>4.39%</td></tr>
    <tr><td>Croatia</td><td>Unprocessed Red Meats</td><td>2010</td><td>2018</td><td>121.65</td><td>171.55</td><td>8</td><td>4.39%</td></tr>
    <tr><td>Laos</td><td>Added Sugars</td><td>1990</td><td>2018</td><td>5.97</td><td>110.00</td><td>28</td><td>10.97%</td></tr>
    <tr><td>Laos</td><td>Non-Starchy Vegetables</td><td>1990</td><td>2018</td><td>42.30</td><td>629.29</td><td>28</td><td>10.12%</td></tr>
    <tr><td>Laos</td><td>Nuts and Seeds</td><td>1990</td><td>2018</td><td>2.49</td><td>14.77</td><td>28</td><td>6.56%</td></tr>
    <tr><td>Myanmar</td><td>Processed Meats</td><td>1990</td><td>2018</td><td>3.83</td><td>46.85</td><td>28</td><td>9.36%</td></tr>
    <tr><td>Myanmar</td><td>Unprocessed Red Meats</td><td>1990</td><td>2018</td><td>10.91</td><td>133.51</td><td>28</td><td>9.36%</td></tr>
    <tr><td>Myanmar</td><td>Eggs</td><td>1990</td><td>2018</td><td>2.14</td><td>25.89</td><td>28</td><td>9.32%</td></tr>
    <tr><td>Vietnam</td><td>Nuts and Seeds</td><td>1990</td><td>2018</td><td>2.68</td><td>32.47</td><td>28</td><td>9.31%</td></tr>
    <tr><td>Vietnam</td><td>Shellfish</td><td>1990</td><td>2018</td><td>3.10</td><td>28.05</td><td>28</td><td>8.19%</td></tr>
    <tr><td>Vietnam</td><td>Cheese</td><td>1990</td><td>2018</td><td>0.05</td><td>0.38</td><td>28</td><td>7.20%</td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    color: #2e3d49; 
    font-size: 17px; 
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
">
Rapid Growth in Microplastic Contamination Across Food Categories  
Examining the fastest-growing microplastic contributors reveals some interesting patterns. Both Belgium and Croatia show particularly high growth in <strong>vegetables</strong>, with Belgium’s <strong>other starchy vegetables</strong> (CAGR 16.95%) and Croatia’s <strong>non-starchy vegetables</strong> (CAGR 18.83%) leading the way, suggesting that shifts in vegetable consumption or processing practices may strongly influence microplastic exposure in Europe.<br>

Meanwhile, animal-derived products like <strong>milk</strong> in Belgium (CAGR 15.29%) and <strong>processed/unprocessed meats</strong> in Croatia also show noticeable growth, highlighting that both plant and animal food chains are important contributors.<br>

In Asia, Laos exhibits striking increases in <strong>non-starchy vegetables</strong> and <strong>added sugars</strong>, while Myanmar and Vietnam show steady growth across <strong>meats, eggs, nuts, and shellfish</strong>, suggesting a more widespread pattern of contamination across multiple food categories.<br>

Overall, this comparison indicates that European countries tend to have very rapid increases in a few dominant food categories, whereas Asian countries display growth that is spread across several food types. Such patterns hint at the influence of local dietary habits, food production, and packaging practices on microplastic exposure.
</p>
""", unsafe_allow_html=True)

insight_section(
    "Africa Has the Most Concentrated Contamination, Driven by Refined Grains",
    "🌍",
    "To better understand the sources of microplastic contamination, we examined whether the exposure in each country is dominated by one or a few food categories or more evenly distributed across multiple categories. For this purpose, we what fraction of calculated how much of the total contamination comes from the single largest food category (Max Share)."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="margin-right: 10px;">
    <p style="text-align:center; font-size:16px; font-weight:bold;">10 Countries with Most Concentrated Contamination</p>
    <table style="font-family: Arial, sans-serif; border-collapse: collapse; width: 100%;">
        <tr style="background-color:#f2f2f2;">
            <th style="border:1px solid #ddd; padding:8px;">Country</th>
            <th style="border:1px solid #ddd; padding:8px;">Mean per Category</th>
            <th style="border:1px solid #ddd; padding:8px;">Std per Category</th>
            <th style="border:1px solid #ddd; padding:8px;">Max Share</th>
        </tr>
        <tr><td>Congo</td><td>77.87</td><td>187.06</td><td>0.579</td></tr>
        <tr><td>Angola</td><td>73.77</td><td>156.07</td><td>0.516</td></tr>
        <tr><td>Togo</td><td>59.50</td><td>131.59</td><td>0.508</td></tr>
        <tr><td>Zimbabwe</td><td>44.61</td><td>89.75</td><td>0.486</td></tr>
        <tr><td>Madagascar</td><td>57.75</td><td>111.78</td><td>0.461</td></tr>
        <tr><td>Cote D'Ivoire</td><td>85.96</td><td>189.79</td><td>0.450</td></tr>
        <tr><td>Tanzania</td><td>72.91</td><td>134.99</td><td>0.445</td></tr>
        <tr><td>Cambodia</td><td>47.70</td><td>89.21</td><td>0.442</td></tr>
        <tr><td>Ethiopia</td><td>43.65</td><td>81.71</td><td>0.425</td></tr>
        <tr><td>Niger</td><td>58.81</td><td>107.94</td><td>0.421</td></tr>
    </table>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="margin-left: 10px;">
    <p style="text-align:center; font-size:16px; font-weight:bold;">10 Countries with Most Widespread Contamination</p>
    <table style="font-family: Arial, sans-serif; border-collapse: collapse; width: 100%;">
        <tr style="background-color:#f2f2f2;">
            <th style="border:1px solid #ddd; padding:8px;">Country</th>
            <th style="border:1px solid #ddd; padding:8px;">Mean per Category</th>
            <th style="border:1px solid #ddd; padding:8px;">Std per Category</th>
            <th style="border:1px solid #ddd; padding:8px;">Max Share</th>
        </tr>
        <tr><td>Spain</td><td>121.87</td><td>138.59</td><td>0.197</td></tr>
        <tr><td>Slovenia</td><td>108.51</td><td>119.82</td><td>0.196</td></tr>
        <tr><td>Colombia</td><td>87.90</td><td>98.54</td><td>0.195</td></tr>
        <tr><td>Cameroon</td><td>97.52</td><td>122.31</td><td>0.194</td></tr>
        <tr><td>Ukraine</td><td>133.36</td><td>152.04</td><td>0.188</td></tr>
        <tr><td>Trinidad And Tobago</td><td>72.12</td><td>75.42</td><td>0.184</td></tr>
        <tr><td>Russia</td><td>120.85</td><td>122.18</td><td>0.178</td></tr>
        <tr><td>Cuba</td><td>102.70</td><td>114.18</td><td>0.171</td></tr>
        <tr><td>Belgium</td><td>111.89</td><td>108.68</td><td>0.157</td></tr>
        <tr><td>Barbados</td><td>139.17</td><td>130.91</td><td>0.147</td></tr>
    </table>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-top: 14px;
    margin-bottom: 20px;
">
It seems that the countries with the most concentrated contamination are mostly African. To investigate this further, we calculated Max Share for each continent. Africa ranks highest with an average share of <strong>33.9%</strong>, meaning that in African countries (within our dataset), the single most contaminated category accounts for about one-third of total microplastic intake. In comparison, the figure is <strong>28.7% in Asia and 27.7% in Oceania</strong>.<br>
</p>
""", unsafe_allow_html=True)

# Continent-level table
st.markdown('<p style="text-align:center; font-size:16px; font-weight:bold;">Average Share of Most Contaminated Food Category per Continent</p>', unsafe_allow_html=True)
st.markdown("""
<table style="font-family: Arial, sans-serif; border-collapse: collapse; width:50%; margin:auto;">
    <tr style="background-color:#f2f2f2;">
        <th style="border:1px solid #ddd; padding:8px;">Continent</th>
        <th style="border:1px solid #ddd; padding:8px;">Max Share</th>
    </tr>
    <tr><td>Africa (AF)</td><td>0.339</td></tr>
    <tr><td>Asia (AS)</td><td>0.287</td></tr>
    <tr><td>Oceania (OC)</td><td>0.277</td></tr>
    <tr><td>Europe (EU)</td><td>0.260</td></tr>
    <tr><td>North America (NA)</td><td>0.245</td></tr>
    <tr><td>South America (SA)</td><td>0.242</td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-top: 14px;
    margin-bottom: 20px;
">
Looking at the top 10 countries with the most concentrated microplastic contamination, we found that in 9 out of 10 of them, the leading category is <strong>refined grains</strong>. As noted earlier, refined grains are also the largest contributor to microplastics globally. They are the biggest source in <strong>41% of countries</strong> in our dataset and are particularly dominant in several African nations. For instance, in <strong>Congo, Angola, and Togo</strong>, refined grains account for <strong>more than 50%</strong> of total contamination (μg/kg). This contamination often originates during <strong>milling, drying, and packaging processes</strong>.<br>
Finally, we checked which category is the biggest contributor across all countries. On average, <strong>refined grains top the list in 44 countries</strong>, followed by <strong>milk (32 countries)</strong> and <strong>non-starchy vegetables (16 countries)</strong>.
</p>
""", unsafe_allow_html=True)

display_chart("output/8_biggest_contributors_count.png")

st.subheader("➡️ Milk is a Strong Predictor of Totals")


st.markdown("""
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">
To complement the main results, we also examined how individual food groups correlate with the overall level of microplastic contamination. This perspective highlights which categories tend to move in step with total contamination and therefore act as key drivers of variation across countries and years. The strongest correlations were found for <strong>milk, unprocessed red meats, and potatoes (correlations above 0.65)</strong>.
</p>      
""", unsafe_allow_html=True)

display_chart("output/7_intermediate_correlation_of_microplastics.png")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">
<strong>Milk</strong> stands out in particular: it is not only among the most contaminated categories on average, but also highly predictive of total contamination levels. <strong>Non-starchy vegetables</strong> show a similar, though slightly weaker, pattern. By contrast, <strong>refined grains</strong>, despite their high average contamination, show little correlation with totals, suggesting they are consistently contaminated across countries rather than driving cross-country differences.
</p>      
               
<p style="
    font-family: 'Arial', sans-serif;
    color: #2e3d49;
    font-size: 17px;
    line-height: 1.7;
    margin-bottom: 20px;
">
Taken together, this indicates that some foods (such as milk and non-starchy vegetables) are both highly contaminated and central to overall exposure patterns, while others (like red meats and potatoes) function more as <strong>“swing factors”</strong>: they may not always be the most contaminated foods, but where they are elevated, they strongly boost the overall contamination totals.
</p>
""", unsafe_allow_html=True)


# ---------------------------
# Closing Callout
# ---------------------------
insight_section(
    "Outlook and Possible Developments",
    "🧩",
    "Here some potential directions for future research."
)

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
">
Together, these findings provide a comprehensive overview of 
<strong>microplastics in our food system</strong>, highlighting urgent challenges 
and pointing to areas for further research. One promising avenue is the use of 
<strong>machine learning algorithms 🤖</strong> to forecast contamination trends, 
which could help predict how microplastic levels might evolve over time and inform 
more proactive interventions.
</p>
""", unsafe_allow_html=True)