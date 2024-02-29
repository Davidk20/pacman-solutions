"""File containing a set of models linking JSON objects to data types."""
from typing import TypedDict


class LevelData(TypedDict):
    """Typed representation of a level as stored in levels.json"""

    name: str
    map: list[list[int]]
    homes: dict[str, list[list[int]]]


class AgentHomes(TypedDict):
    """Typed representation of the agents home paths data structure."""

    pacman: list[tuple[int, int]]
    blinky: list[tuple[int, int]]
    pinky: list[tuple[int, int]]
    inky: list[tuple[int, int]]
    clyde: list[tuple[int, int]]
