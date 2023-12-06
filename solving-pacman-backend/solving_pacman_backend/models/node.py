"""Model representing a node within a graph."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.pickups import Pickup


class Node:
    """
    Model representing a node within a graph.

    As well as storing itself and connected nodes, the nodes will be used to
    encode positional data about the position of the node relative to the level
    as well as what items or agents are currently in that position.
    """

    def __init__(
        self, position: tuple[int, int], agent: Agent = None, pickup: Pickup = None
    ) -> None:
        """
        Initialise a `Node` object.

        Parameters
        ----------
        `position` : `tuple[int, int]`
            Tuple containing the x and y coordinates of
            the node relative to the array.

        `agent` : `Agent`
            The agent which is currently in this space, `None` otherwise.

        `pickup` : `Pickup`
            The pickup which is currently in this space, `None` otherwise.
        """
        if agent and pickup:
            raise ValueError(
                "A newly added Node cannot have both an Agent and Pickup Item."
            )
        self.visited = False
        """`true` if the node has been visited by the Pac-Man agent."""
        self.position = position
        """The position of the node in relation to the array-based level."""
        self.agent = agent
        """Stores the agent currently within this space. `None` otherwise."""
        self.pickup = pickup
        """Stores the item currently within this space. `None` otherwise."""
        self.edges: list[Node] = []
        """List containing all adjacent `Node's`"""
