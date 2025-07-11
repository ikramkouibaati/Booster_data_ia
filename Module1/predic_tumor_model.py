import joblib
import numpy as np

# Charger modèle et scaler une seule fois
model = joblib.load("cancer_model.joblib")
scaler = joblib.load("scaler.joblib")

def predict_tumor(features):
    """
    features : dict avec les clés "size" et "p53_concentration"
    """
    X = np.array([[features["size"], features["p53_concentration"]]])
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)
    return int(prediction[0])
