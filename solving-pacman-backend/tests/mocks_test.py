"""Mock values for use with tests."""
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.services.level_handler import LevelHandler


def mock_graph() -> Graph:
    """Generate a mock version of a graph."""
    level_handler = LevelHandler()
    return level_handler.flood_search(1)
