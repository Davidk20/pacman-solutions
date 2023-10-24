"""Tests for the Agent model."""
import pytest
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.movement_types import MovementTypes


@pytest.fixture(autouse=True)
def agent():
    """Generate an agent instance which can be used for testing."""
    return Agent()


def test_set_movement_type(agent):
    """Test to check that movement type can be correctly set."""
    assert agent.movement_type is None
    agent.set_movement_type(MovementTypes.CUSTOM)
    assert agent.movement_type == MovementTypes.CUSTOM
