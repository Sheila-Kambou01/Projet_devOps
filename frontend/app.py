import streamlit as st
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000/taches/"

st.title("To-Do List avec FastAPI et SQLite")

# Créer une tâche
st.header("Ajouter une tâche")
titre = st.text_input("Titre de la tâche")
description = st.text_area("Description")
date_echeance = st.date_input("Date d'échéance")

if st.button("Ajouter la tâche"):
    data = {
        "titre": titre,
        "description": description,
        "date_echeance": str(date_echeance),
        "utilisateur_id": 1  # Id utilisateur à modifier
    }
    response = requests.post(f"{API_URL}", json=data)
    if response.status_code == 200:
        st.success("Tâche ajoutée avec succès")
    else:
        st.error("Erreur lors de l'ajout de la tâche")

# Récupérer et afficher les tâches
st.header("Mes tâches")
response = requests.get(f"{API_URL}1")  # ID utilisateur = 1
if response.status_code == 200:
    taches = response.json()
    for tache in taches:
        st.write(f"**{tache['titre']}** - {tache['description']} - {tache['date_echeance']}")
else:
    st.error("Erreur lors de la récupération des tâches")
