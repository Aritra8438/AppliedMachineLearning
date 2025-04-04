import os
import time
import requests
import subprocess


def test_docker():
    """Test if the docker container is running"""

    # Check if the Docker image already exists
    check_image = subprocess.run(
        ["docker", "image", "inspect", "flask-app"],
        capture_output=True,
        text=True,
    )

    # Build only if the image doesn't exist
    if check_image.returncode != 0:
        print("Building Docker image...")
        build_process = subprocess.run(
            ["docker", "build", "-t", "flask-app", "."],
            check=True,
            capture_output=True,
            text=True,
        )
        print("Docker image built successfully.")
    else:
        print("Docker image 'flask-app' already exists.")

    print("Starting Docker container...")
    run_process = subprocess.run(
        [
            "docker",
            "run",
            "-d",
            "-p",
            "5000:5000",
            "--name",
            "flask-container",
            "flask-app",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    # Give the container time to start up
    time.sleep(300)

    response = requests.get("http://127.0.0.1:5000/health")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert response.json() == {
        "status": "API is up and running!"
    }, f"Unexpected response: {response.json()}"
    print("Docker container is running successfully.")


def test_docker_home_okay():
    """Test on get method"""
    response = requests.get("http://127.0.0.1:5000/health")
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert response.json() == {
        "status": "API is up and running!"
    }, f"Unexpected response: {response.json()}"


def test_docker_response_has_two_keys():
    """Test to verify that the response contains exactly two keys"""
    response = requests.post("http://127.0.0.1:5000/score", json={"text": "hello"})
    response_data = response.json()
    assert (
        len(response_data.keys()) == 2
    ), f"Expected 2 keys, but got {len(response_data.keys())}"
    assert "prediction" in response_data, "Response should contain 'prediction' key"
    assert "propensity" in response_data, "Response should contain 'propensity' key"


def test_docker_home_post():
    """Test on post method with JSON input"""
    response = requests.post("http://127.0.0.1:5000/score", json={"text": "hello"})
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert "prediction" in response.json(), "Response should contain 'prediction' key"
    assert "propensity" in response.json(), "Response should contain 'propensity' key"
    assert isinstance(
        response.json()["prediction"], str
    ), "Prediction should be a string"
    assert response.json()["prediction"] in [
        "spam",
        "ham",
    ], "Prediction should be either 'spam' or 'ham'"
    assert isinstance(
        response.json()["propensity"], float
    ), "Propensity should be a float"


def test_docker_obvious_spam():
    """Test on obvious spam text"""
    spam_texts = [
        "Congratulations! Claim your free prize today!!!",
        "You are a lucky winner of $500,000! Visit our site to collect!",
        "Alert: Suspicious activity detected. Verify your account immediately.",
    ]

    for text in spam_texts:
        response = requests.post("http://127.0.0.1:5000/score", json={"text": text})
        response_data = response.json()
        prediction = response_data.get("prediction")
        assert prediction == "spam", f"Expected 'spam', but got {prediction}"


def test_docker_obvious_ham():
    """Test on obvious non-spam text"""
    ham_texts = [
        "Can we reschedule our lunch meeting to next week?",
        "Looking forward to catching up with you soon.",
        "Let me know if you need any help with the project.",
    ]

    for text in ham_texts:
        response = requests.post("http://127.0.0.1:5000/score", json={"text": text})
        response_data = response.json()
        prediction = response_data.get("prediction")
        assert prediction == "ham", f"Expected 'ham', but got {prediction}"

    # Stop and remove the container
    print("Stopping Docker container...")
    subprocess.run(["docker", "stop", "flask-container"], check=True)
    print("Removing Docker container...")
    subprocess.run(["docker", "rm", "flask-container"], check=True)
    print("Docker container has been cleaned up.")
