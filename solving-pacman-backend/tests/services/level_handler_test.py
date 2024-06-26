"""Tests for the LevelHandler."""

import pytest
from solving_pacman_backend.exceptions import LevelNotFoundException
from solving_pacman_backend.services import level_handler


def test_get_level():
    """Test that a level is correctly returned."""
    assert level_handler.get_level(1).get("name") == "Level 1"


def test_level_not_found():
    """Test that LevelNotFoundException is correctly called."""
    with pytest.raises(LevelNotFoundException):
        level_handler.get_level(123456)


def test_get_map():
    """Test that a map is correctly returned."""
    assert len(level_handler.get_map(1)) == 31
    assert len(level_handler.get_map(1)[0]) == 28


def test_map_not_found():
    """Test that LevelNotFoundException is correctly called."""
    with pytest.raises(LevelNotFoundException):
        level_handler.get_map(123456)


def test_get_overview():
    """Test that the levels overview is correctly returned."""
    assert level_handler.get_overview() == ["Level 1"]


def test_get_ghost_home():
    assert level_handler.get_home(1, "Blinky") == [(1, 1), (1, 6), (5, 5), (5, 1)]
