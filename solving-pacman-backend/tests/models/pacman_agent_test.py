"""Tests for the Pac-man Agent."""
import pytest
from solving_pacman_backend.models.ghost_agent import GhostAgent
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.pickups import Orange
from solving_pacman_backend.models.pickups import PowerPellet


@pytest.fixture(autouse=True)
def pacman():
    """Generate an agent of Pac-man which can be used for testing."""
    pacmanAgent = PacmanAgent()
    pacmanAgent.current_score = 0
    return pacmanAgent


@pytest.fixture(autouse=True)
def ghost():
    """Generate an agent of a Ghost which can be used for testing."""
    yield GhostAgent()
    # TODO - Once subclasses of GhostAgent are implemented
    # add a random choice which chooses between the different ghosts


def test_increase_score(pacman: PacmanAgent):
    """Test that Pacman's score is correctly increased when consuming items."""
    pacman.handle_consume(Orange())
    assert pacman.get_score() == 500


def test_enable_energizer(pacman: PacmanAgent):
    """Test that when Pac-man consumes a Power Pellet, he is then energized."""
    pacman.handle_consume(PowerPellet())
    assert pacman.energized


def test_valid_ghost_consume(pacman: PacmanAgent, ghost: GhostAgent):
    """Test that Pac-man correctly consumes ghost when energised."""
    pacman.handle_consume(PowerPellet())
    pacman.handle_consume(ghost)
    assert pacman.get_score() == 250


def test_invalid_ghost_consume(pacman: PacmanAgent, ghost: GhostAgent):
    """Test Pac-man loses a life when he consumes a ghost without energizer."""
    pacman.handle_consume(ghost)
    assert pacman.current_lives == 2


def test_valid_multiple_ghost_consume(pacman: PacmanAgent, ghost: GhostAgent):
    """
    Test that when Pac-man consumes multiple ghosts, the score he receives
    correctly scales with the multiplier defined in the rule set.
    """
    pacman.handle_consume(PowerPellet())
    pacman.handle_consume(ghost)
    assert pacman.get_score() == 250
    pacman.handle_consume(ghost)
    assert pacman.get_score() == 650
    pacman.handle_consume(ghost)
    assert pacman.get_score() == 1450
    pacman.handle_consume(ghost)
    assert pacman.get_score() == 3050
