import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/ks-projects-201801.csv")
    df = df[df['state'].isin(['failed', 'successful'])]
    df['launch_year'] = pd.to_datetime(df['launched']).dt.year
    return df

df = load_data()

# Sidebar - filters
st.sidebar.title("Filtres")
category = st.sidebar.selectbox("Choisissez une catégorie :", ["All"] + sorted(df['main_category'].unique().tolist()))
year = st.sidebar.slider("Année de lancement", int(df['launch_year'].min()), int(df['launch_year'].max()), (2012, 2016))

# Filtrage
filtered_df = df[
    (df['launch_year'] >= year[0]) &
    (df['launch_year'] <= year[1])
]
if category != "All":
    filtered_df = filtered_df[filtered_df["main_category"] == category]

# KPI
st.title("📊 Analyse des projets Kickstarter")
col1, col2 = st.columns(2)
with col1:
    st.metric("Nombre de projets", len(filtered_df))
with col2:
    success_rate = (filtered_df['state'] == 'successful').mean() * 100
    st.metric("Taux de réussite", f"{success_rate:.2f} %")

# Histogramme succès/échec
st.subheader("Répartition des succès / échecs")
fig, ax = plt.subplots()
filtered_df['state'].value_counts().plot(kind="bar", ax=ax, color=["red", "green"])
st.pyplot(fig)

# Montant moyen par catégorie
st.subheader("Montant moyen demandé par catégorie")
mean_goal = filtered_df.groupby("main_category")["usd_goal_real"].mean().sort_values()
fig2, ax2 = plt.subplots(figsize=(8, 4))
mean_goal.plot(kind="barh", ax=ax2)
st.pyplot(fig2)
