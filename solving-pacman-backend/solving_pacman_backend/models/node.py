"""Model representing a node within a graph."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.environment import EnvironmentEntity
from solving_pacman_backend.models.pickups import Pickup


class Node:
    """
    Model representing a node within a graph.

    As well as storing itself and connected nodes, the nodes will be used to
    encode positional data about the position of the node relative to the level
    as well as what items or agents are currently in that position.
    """

    def __init__(
        self, position: tuple[int, int], entity: Agent | Pickup | EnvironmentEntity
    ) -> None:
        """
        Initialise a `Node` object.

        Parameters
        ----------
        `position` : `tuple[int, int]`
            Tuple containing the x and y coordinates of
            the node relative to the array.

        `entity` : `Agent | Pickup | EnvironmentEntity`
            The entity which is currently in this space.
        """
        self.visited = False
        """`true` if the node has been visited by the Pac-Man agent."""
        self.position = position
        """The position of the node in relation to the array-based level."""
        self.entity = entity
        """Stores the entity currently within this space."""

    def __str__(self) -> str:
        return f"""
            Position: {self.position},
            Contains: {self.entity}
        """

    def __repr__(self) -> str:
        return f"""
            Position: {self.position},
            Contains: {self.entity}
        """
