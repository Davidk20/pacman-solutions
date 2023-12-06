"""Service to read and manage the levels."""
import json
import os

from solving_pacman_backend.models.node import Node


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

    def get_map(self, level_num: int) -> list[list]:
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

    def flood_search(self, level_num: int) -> list[Node]:
        """
        convert the map into a series of nodes

        Searches the level using "Flood Fill" search to filter out walls
        and leave only the paths which are then used to generate the graph.

        Inspired by https://lvngd.com/blog/flood-fill-algorithm-python/
        """
        full_map = self.get_map(level_num)
        height = len(full_map)
        width = len(full_map[0])
        print(height, width)
        # array to store the nodes once generated
        nodes: list[Node] = []
        # queue to store the positions to be looked into
        queue: list[tuple[int, int]] = [(1, 1)]
        visited = []
        while len(queue) > 0:
            current = queue.pop(0)
            if full_map[current[1]][current[0]] != 99 and current not in visited:
                # if is valid space then build node and add adjacents
                nodes.append(Node(current))
                expansions = [
                    (current[0] + 1, current[1]),
                    (current[0], current[1] + 1),
                    (current[0], current[1] - 1),
                    (current[0] - 1, current[1]),
                ]
                for expansion in expansions:
                    if (
                        expansion[0] < 0
                        or expansion[0] >= width
                        or expansion[1] < 0
                        or expansion[1] >= height
                    ):
                        continue
                    else:
                        queue.append(expansion)

            visited.append(current)
        return nodes
