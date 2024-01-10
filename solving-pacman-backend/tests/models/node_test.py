"""Tests for the Node model."""
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pickups import PacDot


def test_valid_node_initialisation():
    """Valid nodes should be correctly instantiated."""
    test_node = Node((0, 0), PacDot())
    assert isinstance(test_node, Node)
