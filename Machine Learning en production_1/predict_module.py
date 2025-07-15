import joblib
import numpy as np


model = joblib.load("regression.joblib")

def make_prediction(features):
    """
    features = dictionnaire : {"size": 100, "nb_rooms": 3, "garden": 1}
    """
    X = np.array([[features["size"], features["nb_rooms"], features["garden"]]])
    prediction = model.predict(X)
    return prediction.tolist()
