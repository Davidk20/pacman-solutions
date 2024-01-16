"""Generic functions to be applied to instances of Levels."""
from solving_pacman_backend import constants
from solving_pacman_backend.models.graph import Graph


def graph_to_array(graph: Graph) -> list[list[int]]:
    """
    Convert a `Graph` representation of a level into a 2-D array.

    Parameters
    ----------
    `graph` : `Graph`
        The graph to be converted.

    Returns
    -------
    A 2-D list containing the level.
    """
    level = [[99] * constants.PACMAN_BOARD_WIDTH] * constants.PACMAN_BOARD_HEIGHT
    return level
