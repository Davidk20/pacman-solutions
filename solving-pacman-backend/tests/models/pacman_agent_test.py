"""Tests for the Pac-man Agent."""
import pytest
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.pickups import Orange
from solving_pacman_backend.models.pickups import PowerPellet


@pytest.fixture(autouse=True)
def pacman():
    """Generate an agent of Pac-man which can be used for testing."""
    return PacmanAgent()


def test_increase_score(pacman: PacmanAgent):
    """Test that Pacman's score is correctly increased when consuming items."""
    pacman.handle_consume(Orange())
    assert pacman.get_score() == 500


def test_enable_energizer(pacman: PacmanAgent):
    """Test that when Pac-man consumes a Power Pellet, he is then energized."""
    pacman.handle_consume(PowerPellet())
    assert pacman.energized
