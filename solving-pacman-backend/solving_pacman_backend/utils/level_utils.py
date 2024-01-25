"""Generic functions to be applied to instances of Levels."""
from solving_pacman_backend import constants
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.graph import NodeNotFoundException
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pickups import Empty
from solving_pacman_backend.models.pickups import Pickup
from solving_pacman_backend.services import level_handler
from solving_pacman_backend.utils.entity_utils import convert_value_to_entity
from solving_pacman_backend.utils.entity_utils import EntityNotFoundException


def print_level(level: list[list[int]]) -> None:
    """Prints a formatted version of the 2-D array level."""
    for row in level:
        print(row)


def array_to_graph(level_num: int) -> Graph:
    """
    Convert the map from an array into Graph.

    Searches the level using "Flood Fill" search to filter out walls
    and leave only the paths which are then used to generate the graph.

    Inspired by https://lvngd.com/blog/flood-fill-algorithm-python/

    Parameters
    ----------
    `level_num` : `int`
        The level to convert

    Returns
    -------
    A populated `Graph` object.
    """
    full_map = level_handler.get_map(level_num)
    height = len(full_map)
    width = len(full_map[0])
    # queue to store the positions to be looked into
    queue: list[tuple[int, int]] = [first_non_wall_node(full_map)]
    adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {}
    graph = Graph()

    pos = []
    for y in range(len(full_map)):
        for x in range(len(full_map[0])):
            if full_map[y][x] != 99:
                pos.append((x, y))

    while len(queue) > 0:
        current = queue.pop(0)
        if (
            in_bounds(height, width, current)
            and not is_wall(full_map, current)
            and current not in adjacency_list.keys()
        ):
            # if is valid space then build node and add adjacents
            entity = convert_value_to_entity(full_map[current[1]][current[0]])
            graph.add_node(Node(current, entity))
            adjacency_list[current] = []
            expansions = [
                (current[0] + 1, current[1]),
                (current[0], current[1] + 1),
                (current[0], current[1] - 1),
                (current[0] - 1, current[1]),
            ]
            for expansion in expansions:
                if in_bounds(height, width, expansion):
                    if not is_wall(full_map, expansion):
                        adjacency_list[current].append(expansion)
                        queue.append(expansion)
    graph.map_edges(adjacency_list)
    return graph


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


def is_wall(map: list[list[int]], pos: tuple[int, int]) -> bool:
    """
    Checks if the specified space is a `Wall`.

    Parameters
    ----------
    `map` : `list[list[int]]`
        The level to use as reference.
    `pos` : `tuple[int, int]`
        The position to check.

    Returns
    -------
    `True` if the space is filled with a wall.
    """
    return map[pos[1]][pos[0]] == 99


def first_non_wall_node(map: list[list[int]]) -> tuple[int, int]:
    """
    Find and return the first position within the map.

    This should be the upper-leftmost node which is not a wall.

    Parameters
    ----------
    `map` : `list[list[int]]`
        The level to search.

    Returns
    -------
    The position of the first non-wall node.
    """
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] != 99:
                return (x, y)
    raise EntityNotFoundException("No non-wall nodes found.")
