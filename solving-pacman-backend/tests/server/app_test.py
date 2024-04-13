"""
Tests for the Flask application.

Unit tests for the server only cover the scope of unauthorised requests to
ensure they are blocked. Tests of authenticated requests are completed
externally to prevent the crossover of API keys and access with the server
itself.
"""


def test_app(client):
    """Basic test to check functionality of root page."""
    response = client.get("/")
    print(response)
    assert response.status_code == 303


def test_get_overview(client):
    """Test the levels overview endpoint."""
    response = client.get("/get-levels")
    # Unauthorised request should be rejected
    assert response.status_code == 401


def test_get_invalid_board(client):
    """Test the game endpoint."""
    response = client.get("/get-game?level_num=123456")
    # Unauthorised request should be rejected
    assert response.status_code == 401
