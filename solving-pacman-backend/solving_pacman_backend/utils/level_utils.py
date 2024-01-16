"""Generic functions to be applied to instances of Levels."""
from solving_pacman_backend import constants
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.graph import NodeNotFoundException


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
