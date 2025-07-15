import streamlit as st
import pandas as pd

data = pd.DataFrame({
    'lat': [48.8566, 45.75, 43.5297],         
    'lon': [2.3522, 4.85, 5.4474]
})

st.title("Carte des villes")
st.map(data)
