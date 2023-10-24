"""Tests for the Ghost Agent."""
import pytest
from solving_pacman_backend.models.ghost_agent import GhostAgent


@pytest.fixture
def ghost():
    """Generate an agent of a Ghost which can be used for testing."""
    return GhostAgent()
    # TODO - Once subclasses of GhostAgent are implemented
    # add a random choice which chooses between the different ghosts
    # Only if applicable


def test_get_score(ghost: GhostAgent):
    """Test that the score is correctly returned"""
    assert ghost.get_score() == 200
