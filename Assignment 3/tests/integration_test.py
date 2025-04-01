import os
import time
import requests
import subprocess


def test_flask():
    """Test if Flask app is running"""

    # Please change this code accordingly. I'm on my Windows with virtual environment named `venv`.
    # If you are on a linux system, please change the python_location to "./venv/bin/python.exe".
    python_location = "python"  # default for GitHub workflow
    if os.name == "nt":
        python_location = "./venv/Scripts/python.exe"

    process = subprocess.Popen([python_location, "./Assignment 3/app.py"], shell=False)
    time.sleep(5)
    try:
        response = requests.get("http://127.0.0.1:5000/health")
        assert (
            response.status_code == 200
        ), f"Unexpected status code: {response.status_code}"
        assert response.json() == {
            "status": "API is up and running!"
        }, f"Unexpected response: {response.json()}"
        print("Flask app is running successfully.")
    finally:
        process.terminate()
        process.wait()
        print("Flask app has been shut down.")


def test_home_okay(client):
    """Test on get method"""
    response = client.get("/health")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert response.json == {
        "status": "API is up and running!"
    }, f"Unexpected response: {response.json}"


def test_response_has_two_keys(client):
    """Test to verify that the response contains exactly two keys"""
    response = client.post("/score", json={"text": "hello"})
    response_data = response.json
    assert (
        len(response_data.keys()) == 2
    ), f"Expected 2 keys, but got {len(response_data.keys())}"
    assert "prediction" in response_data, "Response should contain 'prediction' key"
    assert "propensity" in response_data, "Response should contain 'propensity' key"


def test_home_post(client):
    """Test on post method with JSON input"""
    response = client.post("/score", json={"text": "hello"})
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert "prediction" in response.json, "Response should contain 'prediction' key"
    assert "propensity" in response.json, "Response should contain 'propensity' key"
    assert isinstance(response.json["prediction"], str), "Prediction should be a string"
    assert response.json["prediction"] in [
        "spam",
        "ham",
    ], "Prediction should be either 'spam' or 'ham'"
    assert isinstance(
        response.json["propensity"], float
    ), "Propensity should be a float"


def test_obvious_spam(client):
    """Test on obvious spam text"""
    spam_texts = [
        "Congratulations! Claim your free prize today!!!",
        "You are a lucky winner of $500,000! Visit our site to collect!",
        "Alert: Suspicious activity detected. Verify your account immediately.",
    ]

    for text in spam_texts:
        response = client.post("/score", json={"text": text})
        response_data = response.json
        prediction = response_data.get("prediction")
        assert prediction == "spam", f"Expected 'spam', but got {prediction}"


def test_obvious_ham(client):
    """Test on obvious non-spam text"""
    ham_texts = [
        "Can we reschedule our lunch meeting to next week?",
        "Looking forward to catching up with you soon.",
        "Let me know if you need any help with the project.",
    ]

    for text in ham_texts:
        response = client.post("/score", json={"text": text})
        response_data = response.json
        prediction = response_data.get("prediction")
        assert prediction == "ham", f"Expected 'ham', but got {prediction}"
