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

    def add_node(self, node: Node) -> None:
        self.level.add_nodes_from([(self.node_count, {"position": node.position})])
        self.node_count += 1
