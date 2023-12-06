"""Tests for the Node model."""
import pytest
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.pickups import PacDot


def test_valid_node_initialisation():
    """Valid nodes should be correctly instantiated."""
    test_node = Node((0, 0), pickup=PacDot())
    assert isinstance(test_node, Node)


def test_invalid_overfilled_node():
    """
    Error should be thrown when a new node contains both an agent and pickup.

    All nodes at time of instantiation should contain only one thing.
    """
    with pytest.raises(ValueError):
        Node((0, 0), agent=PacmanAgent(), pickup=PacDot())
