"""Service to read and manage the levels."""
import json
import os


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
        return self.levels.get(("level " + str(level_num)))

    def get_map(self, level_num: int) -> list[list]:
        """
        Returns only the map for a given level.

        :param level_num: The number of the desired level
        :returns: The map data for the desired level
        """
        return self.levels.get(("level " + str(level_num))).get("map")

    def close(self) -> None:
        """Closes the levels.json file after use."""
        self.__raw_levels.close()
