from flask import Flask, request, jsonify
from predict_module import predict_tumor

app = Flask(__name__)

@app.route("/")
def home():
    return "🔬 API de prédiction des tumeurs"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = predict_tumor(data)
    return jsonify({"is_cancerous": prediction})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
