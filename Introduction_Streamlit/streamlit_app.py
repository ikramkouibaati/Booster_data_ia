import streamlit as st

name = st.text_input("Entrez votre prénom :")

if name:
    st.write(f"Bonjour {name} !")

print("Une interaction a eu lieu dans Streamlit.")
