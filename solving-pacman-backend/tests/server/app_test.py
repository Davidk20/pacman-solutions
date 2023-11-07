"""Tests for the Flask application."""


def test_app(client):
    """Basic test to check functionality of root page."""
    response = client.get("/")
    assert b"<h1 style='color:blue'>Hello There!</h1>" in response.data


def test_get_board(client):
    """Test that the route can return a game board."""
    response = client.get("/get-board?level_num=1")
    assert b"Level 1" in response.data
    assert response.status == "200 OK"
