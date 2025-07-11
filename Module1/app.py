from flask import Flask, request, jsonify
from predict_module import make_prediction

app = Flask(__name__)

@app.route("/")
def home():
    return "🏠 API de prédiction - Bienvenue !"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # Ex : {"size": 100, "nb_rooms": 3, "garden": 1}
    prediction = make_prediction(data)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
