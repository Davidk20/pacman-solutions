"""Model representing the level as a graph data structure."""
import random

from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.environment import EnvironmentEntity
from solving_pacman_backend.models.environment import Teleporter
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

    def __repr__(self) -> str:
        string = ""
        for parent, children in self.level.items():
            string += f"{parent.position}: {[child.position for child in children]}\n"
        return string

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

    def nodes(self) -> list[Node]:
        """
        Returns all of the nodes in the graph.

        Returns
        -------
        A list containing all of the nodes present in the graph.
        """
        return list(self.level.keys())

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
        for node, children in mapping.items():
            parent = self.find_node_by_pos(node)
            self.level[parent] = []
            for child in children:
                self.level[parent].append(self.find_node_by_pos(child))
        # Manual mapping of portal edges. Assumed that there are only two teleporters
        # and so it is a one-to-one mapping.
        portals = self.find_node_by_entity(Teleporter())
        self.level[portals[0]].append(portals[1])
        self.level[portals[1]].append(portals[0])

        # Check that the graph is connected before returning.
        if not self.is_connected():
            raise InvalidGraphConfigurationException(
                "Graph is not connected, check edges"
            )

    def bfs(self, start_pos: tuple[int, int] | Node) -> list[Node]:
        """
        Perform a breadth first search on the graph given a starting point.

        Parameters
        ----------
        `start_pos` : `tuple[int, int] | Node`
            The starting point from which to run the search.

        Returns
        -------
        The `list` containing the path of the dfs search.
        """
        start = (
            self.find_node_by_pos(start_pos)
            if isinstance(start_pos, tuple)
            else start_pos
        )
        visited: list[Node] = []
        stack: list[Node] = [start]

        while len(stack) > 0:
            current = stack.pop(0)
            visited.append(current)
            for child in self.level[current]:
                if child not in visited and child not in stack:
                    stack.append(child)
        return visited

    def is_connected(self) -> bool:
        """
        Checks that the graph is connected.

        In theory, a graph is fully connected if any `Node` is connected to any
        other node and therefore by selecting a random `Node`, the `bfs` function
        should return a path which contains all `Node` objects within the `Graph`.

        Returns
        -------
        `True` if the `Graph` is connected.
        """
        start: Node = random.choice(list(self.level.keys()))
        path = self.bfs(start)
        return len(path) == len(list(self.level.keys()))
