"""Tests for the LevelHandler."""
import pytest
from solving_pacman_backend.services.level_handler import LevelHandler
from solving_pacman_backend.services.level_handler import (
    LevelNotFoundException,
)


@pytest.fixture(scope="session", autouse=True)
def level_handler():
    """Generate an instance of LevelHandler for testing"""
    level_handler = LevelHandler()
    yield level_handler
    level_handler.close()


def test_get_level(level_handler: LevelHandler):
    """Test that a level is correctly returned."""
    assert level_handler.get_level(1).get("name") == "Level 1"


def test_get_map(level_handler: LevelHandler):
    """Test that a map is correctly returned."""
    assert len(level_handler.get_map(1)) == 31
    assert len(level_handler.get_map(1)[0]) == 28


def test_level_not_found(level_handler: LevelHandler):
    """Test that LevelNotFoundException is correctly called."""
    with pytest.raises(LevelNotFoundException):
        level_handler.get_level(123456)


def test_map_not_found(level_handler: LevelHandler):
    """Test that LevelNotFoundException is correctly called."""
    with pytest.raises(LevelNotFoundException):
        level_handler.get_map(123456)


def test_get_overview(level_handler: LevelHandler):
    """Test that the levels overview is correctly returned."""
    assert level_handler.get_overview() == ["Level 1"]


def test_get_ghost_home(level_handler: LevelHandler):
    assert level_handler.get_home(1, "Blinky") == [(1, 1), (1, 6), (5, 5), (5, 1)]


def test_flood_search(level_handler: LevelHandler):
    """
    Tests that the flood search correctly finds all nodes in the first level.

    - In a 28x31 grid, there are 868 possible positions.
    - There are 562 wall points within this grid.
    - 868 - 562 = 306 playable spaces
    """
    graph = level_handler.flood_search(1)
    assert graph.num_of_nodes() == 306
