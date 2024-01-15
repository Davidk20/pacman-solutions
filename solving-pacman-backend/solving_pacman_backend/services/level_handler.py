"""Service to read and manage the levels."""
import json
import os

from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.environment import EnvironmentEntity
from solving_pacman_backend.models.environment import Gate
from solving_pacman_backend.models.environment import Teleporter
from solving_pacman_backend.models.ghost_agent import BlinkyAgent
from solving_pacman_backend.models.ghost_agent import ClydeAgent
from solving_pacman_backend.models.ghost_agent import InkyAgent
from solving_pacman_backend.models.ghost_agent import PinkyAgent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.pickups import Apple
from solving_pacman_backend.models.pickups import Bell
from solving_pacman_backend.models.pickups import Cherry
from solving_pacman_backend.models.pickups import Empty
from solving_pacman_backend.models.pickups import Galaxian
from solving_pacman_backend.models.pickups import Key
from solving_pacman_backend.models.pickups import Melon
from solving_pacman_backend.models.pickups import Orange
from solving_pacman_backend.models.pickups import PacDot
from solving_pacman_backend.models.pickups import Pickup
from solving_pacman_backend.models.pickups import PowerPellet
from solving_pacman_backend.models.pickups import Strawberry


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

    def convert_value_to_entity(self, value: int) -> Pickup | Agent | EnvironmentEntity:
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
                return Empty()
            case 1:
                return PacDot()
            case 2:
                return PowerPellet()
            case 3:
                return Cherry()
            case 4:
                return Strawberry()
            case 5:
                return Orange()
            case 6:
                return Apple()
            case 7:
                return Melon()
            case 8:
                return Galaxian()
            case 9:
                return Bell()
            case 10:
                return Key()
            case 20:
                return Gate()
            case 21:
                return BlinkyAgent()
            case 22:
                return PinkyAgent()
            case 23:
                return InkyAgent()
            case 24:
                return ClydeAgent()
            case 44:
                return PacmanAgent()
            case 88:
                return Teleporter()
            case _:
                raise EntityNotFoundException(f"Entity {value} not found.")

    def in_bounds(self, height: int, width: int, pos: tuple[int, int]) -> bool:
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

    def is_wall(self, map: list[list[int]], pos: tuple[int, int]) -> bool:
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
        queue: list[tuple[int, int]] = [(1, 1)]
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
                self.in_bounds(height, width, current)
                and not self.is_wall(full_map, current)
                and current not in adjacency_list.keys()
            ):
                # if is valid space then build node and add adjacents
                entity = self.convert_value_to_entity(full_map[current[1]][current[0]])
                graph.add_node(Node(current, entity))
                adjacency_list[current] = []
                expansions = [
                    (current[0] + 1, current[1]),
                    (current[0], current[1] + 1),
                    (current[0], current[1] - 1),
                    (current[0] - 1, current[1]),
                ]
                for expansion in expansions:
                    if self.in_bounds(height, width, expansion):
                        if not self.is_wall(full_map, expansion):
                            adjacency_list[current].append(expansion)
                            queue.append(expansion)
        graph.map_edges(adjacency_list)
        return graph


if __name__ == "__main__":
    level_handler = LevelHandler()
    graph = level_handler.flood_search(1)
    print(graph)
