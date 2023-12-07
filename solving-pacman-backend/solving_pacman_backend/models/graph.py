"""Model representing the level as a graph data structure."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.environment import EnvironmentEntity
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pickups import Pickup


class NodeNotFoundException(Exception):
    """Raised when a queried Node cannot be found."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class DuplicateNodeException(Exception):
    """Raised when it is attempted to add a repeated node."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class InvalidGraphConfigurationException(Exception):
    """Raised when the graph does not fit the required configuration."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class Graph:
    """Model representing the level as a graph data structure."""

    def __init__(self) -> None:
        """
        Initialises the Graph.
        """
        self.level: dict[Node, list[Node]] = {}
        """
        The level represented as a graph.

        This is represented in this case as an adjacency list allowing relations
        to be mapped between nodes and their direct adjacents.
        """
        self.node_count = 1
        """The counter used to identify nodes."""

    def num_of_nodes(self) -> int:
        """
        Returns the size of the graph.

        Returns
        -------
        The number of nodes within the graph.
        """
        return len(self.level.keys())

    def num_of_edges(self) -> int:
        """
        Returns the number of edges within the graph.

        Returns
        -------
        The number of edges within the graph
        """
        counter = 0
        for connections in self.level.values():
            counter += len(connections)
        return counter

    def add_node(self, node: Node) -> None:
        """
        Adds a single, unconnected `Node` into the graph.

        Parameters
        ----------
        `node` : `Node`
            The `Node` object to add to the graph.
        """
        if node not in self.level.keys():
            self.level[node] = []
            self.node_count += 1
        else:
            raise DuplicateNodeException("Node already in graph.")

    def find_node_by_pos(self, pos: tuple[int, int]) -> Node:
        """
        Find and return the node at a given position

        Parameters
        ----------
        `pos` : `tuple[int, int]`
            The position to query

        Returns
        -------
        The `Node` with the corresponding position. If none is found then an
        `Exception` is raised.
        """
        for node in self.level.keys():
            if node.position == pos:
                return node
        raise NodeNotFoundException("Node not found.")

    def find_node_by_entity(
        self, item: Agent | Pickup | EnvironmentEntity
    ) -> list[Node]:
        """
        Find and return all `Node` objects on the graph with the corresponding value.

        Parameters
        ----------
        `item` : `Agent | Pickup`
            The item to search for. Can be an `Agent` or `Pickup` item.

        Returns
        -------
        A `List` containing all matching `Node` Objects.
        - If `item == Agent`, the list should only contain one value.
        """
        nodes = []
        for node in self.level.keys():
            if node.entity.value == item.value:
                nodes.append(node)
        if isinstance(item, Agent) and len(nodes) > 1:
            raise InvalidGraphConfigurationException(
                f"Only one of type {item.value} should be present."
            )
        elif len(nodes) == 0:
            raise InvalidGraphConfigurationException(
                f"No instances of {item.value} could be found."
            )
        else:
            return nodes

    def map_edges(self, mapping: dict[tuple[int, int], list[tuple[int, int]]]) -> None:
        """
        Maps nodes to their adjacent nodes.

        Uses a raw adjacency list to build the internal adjacency list structure,
        converting positions into `Node` objects.

        Parameters
        ----------
        `mapping` : `dict[tuple[int, int], list[tuple[int, int]]]`
            The raw mapping between nodes and their adjacent nodes.
        """
        # TODO should check here that graph is fully connected or throw error

        for node, children in mapping.items():
            parent = self.find_node_by_pos(node)
            self.level[parent] = []
            for child in children:
                self.level[parent].append(self.find_node_by_pos(child))
