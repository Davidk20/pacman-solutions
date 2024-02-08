"""Mock values for use with tests."""
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.services import level_handler
from solving_pacman_backend.utils import level_utils


def mock_graph() -> Graph:
    """Generate a mock version of a graph."""
    array = level_handler.get_map(1)
    return level_utils.array_to_graph(array)
