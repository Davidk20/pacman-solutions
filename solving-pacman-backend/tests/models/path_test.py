"""Tests for the Path class."""
import pytest
from solving_pacman_backend.models import environment
from solving_pacman_backend.models import ghost_agent
from solving_pacman_backend.models import pickups
from solving_pacman_backend.models.node import Node


@pytest.fixture(scope="session", autouse=True)
def path_no_agents():
    """Generate a path for testing containing no agents."""
    path = [
        Node((0, 0), pickups.PacDot()),
        Node((0, 1), pickups.PowerPellet()),
        Node((0, 2), pickups.Empty()),
        Node((0, 3), environment.Teleporter()),
        Node((0, 4), environment.Teleporter()),
        Node((0, 5), pickups.PacDot()),
        Node((0, 6), pickups.PacDot()),
        Node((0, 7), pickups.PacDot()),
    ]
    yield path


@pytest.fixture(scope="session", autouse=True)
def path_with_agents():
    """Generate a path for testing containing no agents."""
    path = [
        Node((0, 0), pickups.PacDot()),
        Node((0, 1), pickups.PowerPellet()),
        Node((0, 2), pickups.Empty()),
        Node((0, 3), environment.Teleporter()),
        Node((0, 4), environment.Teleporter()),
        Node((0, 5), pickups.PacDot()),
        Node((0, 6), pickups.PacDot()),
        Node((0, 7), pickups.PacDot()),
        Node((0, 8), ghost_agent.BlinkyAgent([])),
    ]
    yield path
