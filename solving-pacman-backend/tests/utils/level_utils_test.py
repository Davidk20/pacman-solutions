"""Tests on the level utility functions."""
from solving_pacman_backend.utils.level_utils import graph_to_array
from tests import mocks_test


def test_graph_to_array_size():
    """
    Test that the array returned by the conversion function
    is the correct size.
    """
    graph = mocks_test.mock_graph()
    array = graph_to_array(graph)
    assert len(array) == 31
    assert len(array[0]) == 28
