"""Tests for the Flask application."""


def test_app(client):
    """Basic test to check functionality of root page."""
    response = client.get("/")
    assert b"<h1 style='color:blue'>Hello There!</h1>" in response.data
