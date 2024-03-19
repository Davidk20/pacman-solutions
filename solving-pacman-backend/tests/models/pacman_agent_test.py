"""Tests for the Pac-man Agent."""
import pytest
from solving_pacman_backend.models.agents.agent import Agent
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.agents.pacman_agent import PacManDiedException
from solving_pacman_backend.models.pickups import Orange
from solving_pacman_backend.models.pickups import PowerPellet
from tests.mocks.mock_agent_test import mock_ghost


@pytest.fixture(autouse=True)
def pacman():
    """Generate an agent of Pac-man which can be used for testing."""
    pacman_agent = PacmanAgent([(0, 0)])
    return pacman_agent


@pytest.fixture(autouse=True)
def ghost():
    """Generate an agent of a Ghost which can be used for testing."""
    yield mock_ghost()


def test_increase_score(pacman: PacmanAgent):
    """Test that Pacman's score is correctly increased when consuming items."""
    pacman.handle_consume(Orange())
    assert pacman.score() == 500


def test_enable_energizer(pacman: PacmanAgent):
    """Test that when Pac-man consumes a Power Pellet, he is then energized."""
    pacman.handle_consume(PowerPellet())
    assert pacman.energized


def test_valid_ghost_consume(pacman: PacmanAgent, ghost: Agent):
    """Test that Pac-man correctly consumes ghost when energised."""
    pacman.handle_consume(PowerPellet())
    pacman.handle_consume(ghost)
    assert pacman.score() == 250


def test_invalid_ghost_consume(pacman: PacmanAgent, ghost: Agent):
    """Test Pac-man loses a life when he consumes a ghost without energizer."""
    with pytest.raises(PacManDiedException):
        pacman.handle_consume(ghost)


def test_valid_multiple_ghost_consume(pacman: PacmanAgent, ghost: Agent):
    """
    Test that when Pac-man consumes multiple ghosts, the score he receives
    correctly scales with the multiplier defined in the rule set.
    """
    pacman.handle_consume(PowerPellet())
    pacman.handle_consume(ghost)
    assert pacman.score() == 250
    pacman.handle_consume(ghost)
    assert pacman.score() == 650
    pacman.handle_consume(ghost)
    assert pacman.score() == 1450
    pacman.handle_consume(ghost)
    assert pacman.score() == 3050


def test_deenergize(pacman: PacmanAgent, ghost: Agent):
    """Test the de-energize function correctly restores state."""
    pacman.handle_consume(PowerPellet())
    pacman.handle_consume(ghost)
    # At this time, Pac-man should be able to consume
    assert pacman.score() == 250
    pacman.deenergize()
    # After being de-energized, Pac-man should lose a life
    with pytest.raises(PacManDiedException):
        pacman.handle_consume(ghost)
