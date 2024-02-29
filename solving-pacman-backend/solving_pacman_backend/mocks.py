"""Mock values for use with tests or placeholders."""
from solving_pacman_backend.models.ghost_agent import GhostAgent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.movement_types import MovementTypes
from solving_pacman_backend.services import level_handler
from solving_pacman_backend.utils import level_utils


def mock_graph() -> Graph:
    """Generate a mock version of a graph."""
    array = level_handler.get_map(1)
    return level_utils.array_to_graph(array)


def mock_ghost() -> GhostAgent:
    """Generate a mock ghost."""
    return GhostAgent("Blinky", "", MovementTypes.CHASE, [], 0)


def mock_ghosts() -> list[GhostAgent]:
    """Generate a mock of all of the ghosts."""
    return [
        GhostAgent("Blinky", "", MovementTypes.CHASE, [], 0),
        GhostAgent("Pinky", "", MovementTypes.CHASE, [], 0),
        GhostAgent("Inky", "", MovementTypes.CHASE, [], 0),
        GhostAgent("Clyde", "", MovementTypes.CHASE, [], 0),
    ]
