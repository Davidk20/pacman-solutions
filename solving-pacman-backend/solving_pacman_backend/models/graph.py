"""Model representing the level as a graph data structure."""
from solving_pacman_backend.models.node import Node


class NodeNotFoundException(Exception):
    """Raised when a queried Node cannot be found."""

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
        self.level[node] = []
        self.node_count += 1

    def find_node_by_pos(self, pos: tuple[int, int]) -> Node:
        """
        Find and return the node at a given position
        """
        for node in self.level.keys():
            if node.position == pos:
                return node
        raise NodeNotFoundException("Node not found.")

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
