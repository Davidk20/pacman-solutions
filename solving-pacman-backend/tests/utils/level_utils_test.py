"""Tests on the level utility functions."""
from solving_pacman_backend.services import level_handler
from solving_pacman_backend.utils import level_utils
from tests import mocks_test


def test_graph_to_array_size():
    """
    Test that the array returned by the conversion function
    is the correct size.
    """
    graph = mocks_test.mock_graph()
    array = level_utils.graph_to_array(graph)
    assert len(array) == 31
    assert len(array[0]) == 28


def test_graph_to_array_conversion():
    """Test that the conversion is valid."""
    assert level_utils.graph_to_array(mocks_test.mock_graph()) == level_handler.get_map(
        1
    )


def test_array_to_graph():
    """
    Tests that the flood search correctly finds all nodes in the first level.

    - In a 28x31 grid, there are 868 possible positions.
    - There are 562 wall points within this grid.
    - 868 - 562 = 306 playable spaces
    """
    graph = level_utils.array_to_graph(1)
    assert graph.num_of_nodes() == 306


def test_remaining_pickups():
    """
    Test that the number of pickups remaining is correctly counted.

    Taking the assumption that there are 306 playable spaces on the first level,
    once the empty spaces, teleporters and character spaces are taken away this leaves
    241 pickups on the map.
    """
    assert level_utils.remaining_pickups(mocks_test.mock_graph()) == 241


def test_in_bounds():
    assert level_utils.in_bounds(31, 28, (1, 1))


def test_out_of_bounds():
    assert not level_utils.in_bounds(31, 28, (28, 14))


def test_first_non_wall_node():
    assert level_utils.first_non_wall_node(level_handler.get_map(1)) == (1, 1)
