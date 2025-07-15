import streamlit as st
import pandas as pd
import time

#  Définition d'une fonction de chargement de données
@st.cache_data  #  Activer la mise en cache
def load_data():
    time.sleep(5)  #  Simuler un traitement coûteux
    df = pd.read_csv("temperatures.csv")  
    return df


st.title("Démo de st.cache_data")

st.write("Chargement des données en cours...")
df = load_data()
st.success("Données chargées !")

st.write(df)


