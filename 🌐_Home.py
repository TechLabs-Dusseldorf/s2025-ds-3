import streamlit as st

st.set_page_config(
    page_title="PureData | Microplastics in Food", page_icon="🍴", layout="centered"
)

# Title
st.markdown(
    """
    <div style="text-align: center; padding-top: 2rem; font-family: Arial, sans-serif;">
        <h1 style="font-size: 3rem; color: #2f3e46; font-family: Arial, sans-serif;">🥄 PureData</h1>
        <h3 style="color: #2f3e46; font-weight: 400; font-family: Arial, sans-serif;">A Look at Microplastics in Our Food</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<hr>", unsafe_allow_html=True)

# Intro
st.markdown(
    """
    <div style="font-size: 17px; line-height: 1.7; color: #353535; font-family: Arial, sans-serif;">
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
    <div style="font-size: 1rem; color: #353535; font-family: Arial, sans-serif; margin-bottom: 0;">
        <p style="text-align: center;">This project is designed to grow as new research emerges and public awareness evolves.</p>
        <p style="font-style: italic; margin-top: -0.3rem; text-align: center; margin-bottom: 0;">🗺️ Dive into the data. Reflect. Question. Advocate. 🍽️</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Contributors Section
st.markdown(
    """
    <style>
        .contrib-link {
            text-decoration: none;
            color: #1a73e8; /* blue tone */
            font-weight: 500;
            transition: 0.2s;
        }
        .contrib-link:hover {
            text-decoration: underline;
        }
    </style>

    <div style="margin-top: 0.2rem; text-align: center; font-family: Arial, sans-serif;">
        <hr style="margin: 2rem 0; border: none; border-top: 1px solid #e0e0e0;">
        <p style="font-size: 1rem; color: #555;">🤝 Contributors</p>
        <p style="font-size: 1rem;">
            <a class="contrib-link" href="https://github.com/NeginDs" target="_blank">Negin</a> ·
            <a class="contrib-link" href="https://github.com/Nicolem99" target="_blank">Nicole</a> ·
            <a class="contrib-link" href="https://github.com/Humam-Hamdan" target="_blank">Humam</a> ·
            <a class="contrib-link" href="https://github.com/Bionema" target="_blank">Gaetano</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)