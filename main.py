import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Analiza industriei jocurilor video",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main-header {font-size:2.4rem; font-weight:700; color:#6c63ff; text-align:center; margin-bottom:.2rem;}
    .sub-header  {font-size:1.1rem; color:#888; text-align:center; margin-bottom:1.5rem;}
    .section-title {font-size:1.5rem; font-weight:600; color:#6c63ff; margin-top:1rem;}
    </style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/controller.png", width=70)
    st.title("🎮 Navigare")
    sectiune = st.radio(
        "Alege sectiunea:",
        [
            "🏠 Introducere",
            "Exploatare & Valori lipsa",
            "Statistici descriptive",
            "Distributii grafice",
            "Codificare & Scalare",
            "Grupare & Agregare",
            "Clusterizare K-Means",
            "Regresie Logistica",
            "Regresie Multipla (OLS)",
        ],
    )

@st.cache_data
def load_vg():
    return pd.read_csv("vgsales.csv")


# deoarece fisierul este mai mare decat limita de 25gb al github-ului, acesta este link-ul:
# https://www.kaggle.com/datasets/artermiloff/steam-games-dataset?select=games_march2025_full.csv
@st.cache_data
def load_steam():
    return pd.read_csv("games_march2025_full.csv")

vg    = load_vg()
steam = load_steam()

# Introducerea
if sectiune == "🏠 Introducere":
    st.markdown('<p class="main-header">🎮 Analiza industriei jocurilor video pe Steam</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Proiect Python · games_march2025_full.csv</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Nr. jocuri", f"{len(steam):,}")
    col2.metric("Nr. coloane", steam.shape[1])
    col3.metric("Perioada", "2025")

    st.markdown("---")
    st.subheader("Preview date")
    st.dataframe(
        steam[["name", "release_date", "price", "genres",
               "positive", "negative", "metacritic_score",
               "average_playtime_forever", "peak_ccu",
               "recommendations"]].head(10),
        use_container_width=True
    )

    st.info("""
    **Obiective proiect:**
    - Analiza catalogului Steam pe genuri, preț și engagement
    - Identificarea factorilor care influențează succesul unui joc
    - Clusterizare, regresie logistică și multiplă pentru decizii de extindere
    """)