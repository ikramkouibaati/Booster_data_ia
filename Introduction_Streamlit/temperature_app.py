import streamlit as st
import pandas as pd

st.title("Historique des températures")
df = pd.read_csv("temperatures.csv")
df.columns = ["Température"]


st.line_chart(df)

st.write("Tableau des températures :")
st.dataframe(df)
