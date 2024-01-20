"""Service to read and manage the levels."""
import json
import os

from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.utils.entity_utils import convert_value_to_entity
from solving_pacman_backend.utils.entity_utils import EntityNotFoundException
from solving_pacman_backend.utils.level_utils import in_bounds
from solving_pacman_backend.utils.level_utils import is_wall


class LevelNotFoundException(Exception):
    """Raised when a level is not found"""

    def __init__(self, level_num: int) -> None:
        message = f"Level {level_num} not found."
        super().__init__(message)


class LevelHandler:
    """Service to read and manage the levels."""

    def __init__(self) -> None:
        absolute_path = os.path.dirname(__file__)
        relative_path = "../models/levels.json"
        self.__raw_levels = open(os.path.join(absolute_path, relative_path))
        self.levels: dict = json.load(self.__raw_levels)

    def get_level(self, level_num: int) -> dict:
        """
        Returns all info for a level when provided with the level number.

        :param level_num: The number of the desired level
        :returns: The level data for the desired level
        """
        level = self.levels.get(("level " + str(level_num)))
        if level is None:
            raise LevelNotFoundException(level_num)
        else:
            return level

    def get_map(self, level_num: int) -> list[list[int]]:
        """
        Returns only the map for a given level.

        :param level_num: The number of the desired level
        :returns: The map data for the desired level
        """
        level = self.levels.get(("level " + str(level_num)))
        if level is None:
            raise LevelNotFoundException(level_num)
        else:
            return level.get("map")

    def get_overview(self) -> list[str]:
        """
        Returns an overview of all levels.

        Returns
        -------
        A list of all of the available levels to be solved.
        """
        available = []
        level: dict
        for level in self.levels.values():
            available.append(level.get("name"))
        return available

    def close(self) -> None:
        """Closes the levels.json file after use."""
        self.__raw_levels.close()

    def first_non_wall_node(self, map: list[list[int]]) -> tuple[int, int]:
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

    def flood_search(self, level_num: int) -> Graph:
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
        full_map = self.get_map(level_num)
        height = len(full_map)
        width = len(full_map[0])
        # queue to store the positions to be looked into
        queue: list[tuple[int, int]] = [self.first_non_wall_node(full_map)]
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


if __name__ == "__main__":
    level_handler = LevelHandler()
    graph = level_handler.flood_search(1)
    print(graph)
