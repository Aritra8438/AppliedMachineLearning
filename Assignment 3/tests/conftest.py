import pytest
from app import app


@pytest.fixture
def client():
    """Fixture to provide a test client for the Flask app."""
    app.testing = True
    with app.test_client() as client:
        yield client
