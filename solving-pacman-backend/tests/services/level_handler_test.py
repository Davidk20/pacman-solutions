"""Tests for the LevelHandler."""
import pytest
from solving_pacman_backend.services.level_handler import LevelHandler


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
