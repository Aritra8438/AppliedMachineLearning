import string
import nltk
from nltk.corpus import stopwords
import warnings
import sklearn
import sklearn.pipeline

nltk.download("stopwords")
nltk.download('punkt_tab')
warnings.filterwarnings("ignore")


def preprocess_text(text):
    """
    Preprocesses text by converting to lowercase, removing punctuation and stopwords.
    Args:
        text (str): Input text to preprocess
    Returns:
        str: Cleaned text in lowercase with punctuation and stopwords removed
    """
    text = text.lower()
    words = nltk.word_tokenize(text)

    processed_text = [
        word
        for word in words
        if (
            word.isalnum()
            and word not in stopwords.words("english")
            and word not in string.punctuation
        )
    ]
    text = " ".join(processed_text)
    return text


def score(
    text: str,
    model: sklearn.base.BaseEstimator,
    threshold: float,
    vectorizer: sklearn.feature_extraction.text.TfidfVectorizer,
) -> tuple[bool, float]:
    """
    Classify a text input using a trained model and a specified threshold.
    This function preprocesses the input text, transforms it using a vectorizer,
    and predicts whether the text meets the classification criteria based on the threshold.
    Args:
        text: The input text to classify.
        model: A trained sklearn model for classification.
        threshold: The threshold for converting probabilities into binary predictions.
        vectorizer: A vectorizer to transform the input text.
    Returns:
        tuple: A tuple containing:
            - prediction (bool): True if the text is spam, False otherwise.
            - propensity (float): The probability score for the positive class.
    """
    preprocessed_text = preprocess_text(text)

    text_vectorized = vectorizer.transform([preprocessed_text])

    propensity = model.predict_proba(text_vectorized)[:, 1][0]
    prediction = True if propensity >= threshold else False
    return prediction, propensity
