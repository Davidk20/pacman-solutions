"""Tests on the level utility functions."""
from solving_pacman_backend.services.level_handler import LevelHandler
from solving_pacman_backend.utils.level_utils import graph_to_array
from solving_pacman_backend.utils.level_utils import in_bounds
from solving_pacman_backend.utils.level_utils import remaining_pickups
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


def test_graph_to_array_conversion():
    """Test that the conversion is valid."""
    level_handler = LevelHandler()
    assert graph_to_array(mocks_test.mock_graph()) == level_handler.get_map(1)


def test_remaining_pickups():
    """
    Test that the number of pickups remaining is correctly counted.

    Taking the assumption that there are 306 playable spaces on the first level,
    once the empty spaces, teleporters and character spaces are taken away this leaves
    241 pickups on the map.
    """
    assert remaining_pickups(mocks_test.mock_graph()) == 241


def test_in_bounds():
    assert in_bounds(31, 28, (1, 1))


def test_out_of_bounds():
    assert not in_bounds(31, 28, (28, 14))
