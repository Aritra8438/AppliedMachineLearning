from flask import Flask, request, jsonify
from score import score
import pickle

app = Flask(__name__)


def load_model_and_vectorizer():
    """Helper function to load the model and vectorizer"""
    with open("./best_model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("./tfidf_vectorizer.pkl", "rb") as file:
        vectorizer = pickle.load(file)

    return model, vectorizer


@app.route("/health", methods=["GET"])
def health_check():
    """Endpoint for checking the health of the API"""
    return jsonify(
        {
            "status": "API is up and running!",
        }
    )


@app.route("/score", methods=["POST"])
def score_endpoint():
    """Endpoint for classifying text as spam or ham"""
    data = request.get_json()
    text = data.get("text", "")
    threshold = float(data.get("threshold", 0.5))

    model, vectorizer = load_model_and_vectorizer()
    prediction, propensity = score(text, model, threshold, vectorizer)

    return jsonify(
        {
            "prediction": "spam" if prediction is True else "ham",
            "propensity": propensity,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
