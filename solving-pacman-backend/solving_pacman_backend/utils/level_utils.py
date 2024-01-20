"""Generic functions to be applied to instances of Levels."""
from solving_pacman_backend import constants
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.graph import NodeNotFoundException
from solving_pacman_backend.models.pickups import Empty
from solving_pacman_backend.models.pickups import Pickup


def print_level(level: list[list[int]]) -> None:
    """Prints a formatted version of the 2-D array level."""
    for row in level:
        print(row)


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
    level = []
    for row in range(constants.PACMAN_BOARD_HEIGHT):
        level.append([])
        for column in range(constants.PACMAN_BOARD_WIDTH):
            try:
                node = graph.find_node_by_pos((column, row))
                level[row].append(node.entity.value)
            except NodeNotFoundException:
                level[row].append(99)
                continue
    return level


def remaining_pickups(graph: Graph) -> int:
    """
    Counts the number of pickups remaining on the level.

    Parameters
    ----------
    `graph` : `Graph`
        The level to count.

    Returns
    -------
    The number of non-empty nodes on the graph.
    """
    count = 0
    for node in graph.nodes():
        if isinstance(node.entity, Pickup) and not isinstance(node.entity, Empty):
            count += 1
    return count


def in_bounds(height: int, width: int, pos: tuple[int, int]) -> bool:
    """
    Check a position is within the bounds of the map.

    Parameters
    ----------
    `height` : `int`
        The height of the map.
    `width` : `int`
        The width of the map.
    `pos` : `tuple[int, int]`
        The position to check

    Returns
    -------
    `True` if the position is within bounds.
    """
    return pos[0] >= 0 and pos[0] < width and pos[1] >= 0 and pos[1] < height
