import requests

url = "http://localhost:5000/predict"

examples = [
    {"size": 0.012, "p53_concentration": 0.002},
    {"size": 0.010, "p53_concentration": 0.006},
    {"size": 0.018, "p53_concentration": 0.001},
    {"size": 0.015, "p53_concentration": 0.003},
    {"size": 0.009, "p53_concentration": 0.005},
    {"size": 0.011, "p53_concentration": 0.004},
    {"size": 0.007, "p53_concentration": 0.006},
    {"size": 0.016, "p53_concentration": 0.002},
    {"size": 0.013, "p53_concentration": 0.003},
    {"size": 0.014, "p53_concentration": 0.004}
]

for i, data in enumerate(examples, 1):
    res = requests.post(url, json=data)
    print(f"Exemple {i} ➤ Prediction : {res.json()['is_cancerous']}")
