"""Model representing the level as a graph data structure."""
import networkx as nx
from solving_pacman_backend.models.node import Node


class Graph:
    """Model representing the level as a graph data structure."""

    def __init__(self) -> None:
        """
        Initialises the Graph.
        """
        self.level = nx.Graph()
        """The level represented as a graph."""
        self.node_count = 1
        """The counter used to identify nodes."""

    def size(self) -> int:
        """
        Returns the size of the graph.

        Returns
        -------
        The number of nodes within the graph.
        """
        return len(self.level)

    def add_node(self, node: Node) -> None:
        """
        Adds a single, unconnected `Node` into the graph.

        Parameters
        ----------
        `node` : `Node`
            The `Node` object to add to the graph.
        """
        self.level.add_nodes_from([(self.node_count, {"position": node.position})])
        self.node_count += 1

    def map_edges(self, mapping: dict[tuple[int, int], list[tuple[int, int]]]) -> None:
        """
        Connects all nodes together using the
        """
        # TODO should check here that graph is fully connected or throw error
        node_pos = list(mapping.keys())
        for pos, connections in mapping.items():
            parent = node_pos.index(pos) + 1
            for connection in connections:
                child = node_pos.index(connection) + 1
                self.level.add_edge(parent, child)
