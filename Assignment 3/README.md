<!-- @format -->

# Assignment 3: Flask Server for Spam Classification

This repository contains a simple flask server that serves an implementation of a spam classification system using machine learning.

## Files and Directories

### 1. [`score.py`](./score.py)

This file contains the core functionality for preprocessing text and scoring it using a trained machine learning model.

#### Key Functions:

- **`preprocess_text(text)`**:

  - Converts text to lowercase, removes punctuation, and filters out stopwords.
  - Returns cleaned text.

- **`score(text, model, threshold, vectorizer)`**:
  - Classifies input text as spam or ham using a trained model and a specified threshold.
  - Returns a tuple containing the prediction (True for spam, False for ham) and the probability score.

### 2. [`app.py`](./app.py)

The `app.py` contains a flask server that implements the spam/ham classification system.
It has two endpoints:

- `/health` - get request to test if the server is healthy.
- `/score` - post request to implement the text classification system

### 3. [`tests/`](./tests)

The `/tests` folder currently contains 3 important files:

- [`conftest.py`](./tests/conftest.py) - contains the configuration for the integration tests.
- [`integration_test.py`](./tests/integration_test.py) - contains integration tests which include running the flask server and closing it.
- [`unit_test.py`](./tests/unit_test.py) - contains unit tests that test the score api.

## Comments

I have also added the [`pytest`](https://github.com/Aritra8438/AppliedMachineLearning/actions) and [`codecov`](https://app.codecov.io/gh/Aritra8438/AppliedMachineLearning?search=&displayType=list) (to view code coverage reports) to the github workflows.
