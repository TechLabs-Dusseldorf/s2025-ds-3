import streamlit as st

st.set_page_config(
    page_title="The Dataset", page_icon="📈", layout="centered"
)

st.title("📈 The Dataset")

st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 25px;
">
The dataset used for this analysis was provided by the <strong>PurePlate Initiative</strong>, a global non-profit advocacy group dedicated to promoting food safety and raising awareness about emerging contaminants in the human diet. 
The initiative focuses on the growing presence of <strong>microplastics in our food</strong> and its potential long-term health implications.
</p>
""", unsafe_allow_html=True)

# Stat cards
def stat_card(title, value, icon=""):
    st.markdown(f"""
    <div style="
        background-color: #fffafa; 
        padding: 20px 0; 
        border-radius: 12px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-bottom: 30px;
    ">
        <div style="font-size: 28px;">{icon} {value}</div>
        <div style="font-size: 14px; color: #555;">{title}</div>
    </div>
    """, unsafe_allow_html=True)

stats = [
    {"title": "Countries", "value": 120, "icon": "🌍"},
    {"title": "Food Categories", "value": 18, "icon": "🌽"},
    {"title": "Years of Data", "value": 28, "icon": "⏳"},
]

cols = st.columns(len(stats), gap="medium")
for col, stat in zip(cols, stats):
    with col:
        stat_card(stat['title'], stat['value'], stat['icon'])

file_path = "./processed_microplastics.csv"

with open(file_path, "rb") as f:
    csv_data = f.read()

# Audience callouts
st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 10px;
">
Our findings can be used to inform <strong>public health campaigns</strong>, influence dietary guidelines, and advocate for stricter regulations on plastic production and waste management.
</p>
""", unsafe_allow_html=True)

# Dataset download button
st.markdown("""
<p style="
    font-family: 'Arial', sans-serif; 
    color: #2e3d49; 
    font-size: 17px; 
    line-height: 1.7;
    margin-bottom: 15px;
">
For transparency and to encourage further research, the dataset is available for download below.
</p>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    div.stDownloadButton > button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.download_button(
    label="📥 Download the Dataset",
    data=csv_data,
    file_name="microplastics_dataset.csv",
    mime="text/csv"
)