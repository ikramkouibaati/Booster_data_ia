import requests

url = "http://localhost:5000/predict"


payload = {
    "size": 120,
    "nb_rooms": 4,
    "garden": 1
}

# POST la requête avec JSON
response = requests.post(url, json=payload)


if response.status_code == 200:
    data = response.json()
    print("✅ Prédiction :", data["prediction"])
else:
    print("❌ Erreur :", response.status_code)
