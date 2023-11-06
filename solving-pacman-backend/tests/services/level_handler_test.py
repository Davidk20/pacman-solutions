"""Tests for the LevelHandler."""
import pytest
from solving_pacman_backend.services.level_handler import LevelHandler


@pytest.fixture(autouse=True)
def level_handler():
    """Generate an instance of LevelHandler for testing"""
    return LevelHandler()


def test_get_level(level_handler: LevelHandler):
    """Test that a level is correctly returned."""
    assert level_handler.get_level(1).get("name") == "Level 1"
