from solving_pacman_backend.models import agent
from solving_pacman_backend.models import environment
from solving_pacman_backend.models import pacman_agent
from solving_pacman_backend.models import pickups
from solving_pacman_backend.models.ghost_agent import GhostAgent
from solving_pacman_backend.models.movement_types import MovementTypes


class EntityNotFoundException(Exception):
    """Raised when a queried entity cannot be found."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


def convert_value_to_entity(
    value: int,
) -> pickups.Pickup | agent.Agent | environment.EnvironmentEntity:
    """
    Convert a numerical value into a game entity.

    Parameters
    ----------
    `value` : `int`
        The value taken from the array.

    Returns
    -------
    The entity corresponding to the value.
    """
    match value:
        case 0:
            return pickups.Empty()
        case 1:
            return pickups.PacDot()
        case 2:
            return pickups.PowerPellet()
        case 3:
            return pickups.Cherry()
        case 4:
            return pickups.Strawberry()
        case 5:
            return pickups.Orange()
        case 6:
            return pickups.Apple()
        case 7:
            return pickups.Melon()
        case 8:
            return pickups.Galaxian()
        case 9:
            return pickups.Bell()
        case 10:
            return pickups.Key()
        case 20:
            return environment.Gate()
        case 21:
            return GhostAgent("Blinky", "Shadow", MovementTypes.CHASE, [], 21, 200)
        case 22:
            return GhostAgent("Pinky", "Shadow", MovementTypes.CHASE, [], 21, 200)
        case 23:
            return GhostAgent("Inky", "Shadow", MovementTypes.CHASE, [], 21, 200)
        case 24:
            return GhostAgent("Clyde", "Shadow", MovementTypes.CHASE, [], 21, 200)
        case 44:
            return pacman_agent.PacmanAgent([])
        case 88:
            return environment.Teleporter()
        case _:
            raise EntityNotFoundException(f"Entity {value} not found.")
