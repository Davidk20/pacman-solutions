"""Tests for the Pac-man Agent."""
import pytest
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.pickups import Orange


@pytest.fixture(autouse=True)
def pacman():
    """Generate an agent instance which can be used for testing."""
    return PacmanAgent()


def test_increase_score(pacman: PacmanAgent):
    """Test that Pacman's score is correctly increased when consuming items."""
    pacman.handle_consume(Orange())
    assert pacman.get_score() == 500
