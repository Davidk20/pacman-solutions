"""Mock values for agents."""
from solving_pacman_backend.models.agents.ghost_agent import GhostAgent
from solving_pacman_backend.models.movement_types import MovementTypes


def mock_ghost() -> GhostAgent:
    """Generate a mock ghost."""
    return GhostAgent("Blinky", "", MovementTypes.CHASE, [], 21, 200)


def mock_ghosts() -> list[GhostAgent]:
    """Generate a mock of all of the ghosts."""
    return [
        GhostAgent("Blinky", "", MovementTypes.CHASE, [], 21, 200),
        GhostAgent("Pinky", "", MovementTypes.CHASE, [], 22, 200),
        GhostAgent("Inky", "", MovementTypes.CHASE, [], 23, 200),
        GhostAgent("Clyde", "", MovementTypes.CHASE, [], 24, 200),
    ]
