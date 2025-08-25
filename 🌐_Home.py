import streamlit as st

st.set_page_config(
    page_title="PureData | Microplastics in Food", page_icon="🍴", layout="centered"
)

# Title
st.markdown(
    """
    <div style="text-align: center; padding-top: 2rem; font-family: Arial, sans-serif;">
        <h1 style="font-size: 3rem; color: #2f3e46; font-family: Arial, sans-serif;">🥄 PureData</h1>
        <h3 style="color: #52796f; font-weight: 400; font-family: Arial, sans-serif;">A Look at Microplastics in Our Food</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# Intro
st.markdown(
    """
    <div style="font-size: 1.05rem; line-height: 1.7; color: #353535; font-family: Arial, sans-serif;">
        <p><strong>PureData</strong> is a data-driven companion to the <strong>PurePlate Initiative</strong> — an effort to explore the hidden presence of <em>microplastics</em> in our diets and their potential health impact.</p>
        <p>This dashboard presents findings from research and modeling based on global consumption data. You're invited to explore:</p>
        <ul>
            <li>📉 <strong>Trends</strong> in microplastic consumption</li>
            <li>🥫 <strong>High-risk food categories</strong></li>
            <li>🌍 <strong>Geographic patterns</strong> of exposure</li>
            <li>🧠 <strong>Health implications</strong> and uncertainties</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# Closing Section
st.markdown(
    """
    <div style="font-size: 1rem; color: #555555; font-family: Arial, sans-serif;">
        <p style="text-align: center;">This project is designed to grow as new research emerges and public awareness evolves.</p>
        <p style="font-style: italic; margin-top: -0.3rem; text-align: center;">🗺️ Dive into the data. Reflect. Question. Advocate. 🍽️</p>
    </div>
    """,
    unsafe_allow_html=True,
)
