from score import score
import pickle

with open("./Assignment 3/best_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("./Assignment 3/tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def test_score():
    """Smoke test for the score function"""
    text = "Hello, this is a test message!"
    prediction, propensity = score(text, model, 0.5, vectorizer)
    # Basic smoke test - function runs without errors
    assert True, "Score function should run without errors"

    # Check return value types and ranges
    assert isinstance(prediction, int) and prediction in [
        0,
        1,
    ], "Prediction should be an integer (0 or 1)"
    assert (
        isinstance(propensity, float) and 0 <= propensity <= 1
    ), "Propensity should be a float between 0 and 1"


def test_score_format():
    """Test input/output formats/types"""
    text = "Another test message"
    prediction, propensity = score(text, model, 0.5, vectorizer)

    assert isinstance(prediction, int), "Prediction should be an integer"
    assert prediction in [0, 1], "Prediction should be either 0 or 1"

    assert isinstance(propensity, float), "Propensity should be a float"
    assert 0 <= propensity <= 1, "Propensity should be between 0 and 1"


def test_prediction_values():
    """Test if prediction is either 0 or 1"""
    texts = [
        "Free money now!!!",
        "Hello, how are you doing today?",
        "This is a neutral message",
    ]

    for text in texts:
        prediction, _ = score(text, model, 0.5, vectorizer)
        assert prediction in [0, 1], f"Prediction should be 0 or 1, got {prediction}"


def test_propensity_range():
    """Test if propensity score is between 0 and 1"""
    test_cases = [
        "Win a free iPhone! Click now!",
        "Meeting tomorrow at 10am",
        "This is a spam message",
        "Regular business inquiry",
        "URGENT: Your account needs attention!!!",
    ]

    for text in test_cases:
        _, propensity = score(text, model, 0.5, vectorizer)
        assert isinstance(
            propensity, float
        ), f"Propensity should be a float, got {type(propensity)}"
        assert (
            0 <= propensity <= 1
        ), f"Propensity should be between 0 and 1, got {propensity}"


def test_threshold_zero():
    """Test if threshold=0 makes prediction always 1"""
    test_cases = [
        "This should be ham",
        "Normal message",
        "Regular email content",
    ]
    for text in test_cases:
        prediction, _ = score(text, model, 0.0, vectorizer)
        assert (
            prediction == 1
        ), f"With threshold=0, prediction should be 1, got {prediction}"


def test_threshold_one():
    """Test if threshold=1 makes prediction always 0"""
    test_cases = [
        "FREE MONEY!!!",
        "Urgent! Click this link!",
        "You've won a prize",
    ]
    for text in test_cases:
        prediction, _ = score(text, model, 1.0, vectorizer)
        assert (
            prediction == 0
        ), f"With threshold=1, prediction should be 0, got {prediction}"


def test_obvious_spam():
    """Test on obvious spam text"""
    spam_texts = [
        "FREE FREE FREE get your free gift now!!!",
        "You've won $1,000,000! Click here to claim!",
        "Urgent: Your account has been compromised. Send password to reset.",
    ]
    for text in spam_texts:
        prediction, _ = score(text, model, 0.5, vectorizer)
        assert (
            prediction == 1
        ), f"Expected prediction=1 for spam text, but got {prediction}."


def test_obvious_ham():
    """Test on obvious non-spam text"""
    ham_texts = [
        "Hello, how are you doing today?",
        "The meeting is scheduled for tomorrow at 3pm.",
        "Please find attached the report we discussed yesterday.",
    ]
    for text in ham_texts:
        prediction, _ = score(text, model, 0.5, vectorizer)
        assert (
            prediction == 0
        ), f"Expected prediction=0 for ham text, but got {prediction}."
