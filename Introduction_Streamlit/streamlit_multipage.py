import streamlit as st


st.write("Session State complet :", st.session_state)

if "page" not in st.session_state:
    st.session_state["page"] = "accueil"


st.sidebar.title("Navigation")
if st.sidebar.button("Accueil"):
    st.session_state["page"] = "accueil"
if st.sidebar.button("Page 2"):
    st.session_state["page"] = "page2"


if st.session_state["page"] == "accueil":
    st.header("Coucou page accueil ")
elif st.session_state["page"] == "page2":
    st.header("Coucou page 2 📄")
