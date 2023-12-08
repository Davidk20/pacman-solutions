"""Service to read and manage the levels."""
import json
import os

from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.node import Node


class LevelNotFoundException(Exception):
    """Raised when a level is not found"""

    def __init__(self, level_num: int) -> None:
        message = f"Level {level_num} not found."
        super().__init__(message)


class EntityNotFoundException(Exception):
    """Raised when a queried entity cannot be found."""

    def __init__(self, message: str) -> None:
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

    def flood_search(self, level_num: int) -> Graph:
        """
        convert the map into a series of nodes

        Searches the level using "Flood Fill" search to filter out walls
        and leave only the paths which are then used to generate the graph.

        Inspired by https://lvngd.com/blog/flood-fill-algorithm-python/
        """
        full_map = self.get_map(level_num)
        height = len(full_map)
        width = len(full_map[0])
        # queue to store the positions to be looked into
        # TODO replace (1,1) with first non-wall node
        queue: list[tuple[int, int]] = [(1, 1)]
        adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {}
        graph = Graph()

        def is_valid(coord: tuple[int, int]) -> bool:
            # TODO refactor into one line
            if (
                coord[0] >= 0
                and coord[0] < width
                and coord[1] >= 0
                and coord[1] < height
            ):
                return full_map[coord[1]][coord[0]] != 99
            else:
                return False

        pos = []
        for y in range(len(full_map)):
            for x in range(len(full_map[0])):
                if full_map[y][x] != 99:
                    pos.append((x, y))

        while len(queue) > 0:
            current = queue.pop(0)
            if is_valid(current) and current not in adjacency_list.keys():
                # if is valid space then build node and add adjacents
                graph.add_node(Node(current))
                adjacency_list[current] = []
                expansions = [
                    (current[0] + 1, current[1]),
                    (current[0], current[1] + 1),
                    (current[0], current[1] - 1),
                    (current[0] - 1, current[1]),
                ]
                for expansion in expansions:
                    if is_valid(expansion):
                        adjacency_list[current].append(expansion)
                        queue.append(expansion)
        graph.map_edges(adjacency_list)
        return graph
