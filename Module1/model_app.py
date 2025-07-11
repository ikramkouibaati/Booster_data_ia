import streamlit as st
import joblib
import requests

st.title("🏡 Estimation du prix d'une maison")

model = joblib.load("regression.joblib")

size = st.number_input("Taille (en m²)", value=100)
nb_rooms = st.number_input("Nombre de chambres", value=3)
garden = st.selectbox("Jardin ?", options=["Oui", "Non"])
garden_value = 1 if garden == "Oui" else 0

if st.button("Prédire via API Flask"):
    payload = {
        "size": size,
        "nb_rooms": nb_rooms,
        "garden": garden_value
    }
    response = requests.post("http://localhost:5000/predict", json=payload)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"💰 Prix estimé : **{prediction[0]:,.2f} €**")
    else:
        st.error("❌ Erreur lors de l’appel à l’API")

