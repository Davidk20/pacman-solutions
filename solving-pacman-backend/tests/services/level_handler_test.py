"""Tests for the LevelHandler."""
import pytest
from solving_pacman_backend.services.level_handler import get_home
from solving_pacman_backend.services.level_handler import get_level
from solving_pacman_backend.services.level_handler import get_map
from solving_pacman_backend.services.level_handler import get_overview
from solving_pacman_backend.services.level_handler import LevelNotFoundException


def test_get_level():
    """Test that a level is correctly returned."""
    assert get_level(1).get("name") == "Level 1"


def test_level_not_found():
    """Test that LevelNotFoundException is correctly called."""
    with pytest.raises(LevelNotFoundException):
        get_level(123456)


def test_get_map():
    """Test that a map is correctly returned."""
    assert len(get_map(1)) == 31
    assert len(get_map(1)[0]) == 28


def test_map_not_found():
    """Test that LevelNotFoundException is correctly called."""
    with pytest.raises(LevelNotFoundException):
        get_map(123456)


def test_get_overview():
    """Test that the levels overview is correctly returned."""
    assert get_overview() == ["Level 1"]


def test_get_ghost_home():
    assert get_home(1, "Blinky") == [(1, 1), (1, 6), (5, 5), (5, 1)]
