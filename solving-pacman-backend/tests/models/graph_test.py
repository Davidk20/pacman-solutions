import pytest
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.node import Node


@pytest.fixture(scope="session", autouse=True)
def graph():
    """Generate an instance of Graph for testing"""
    graph = Graph()
    yield graph


@pytest.fixture(scope="session", autouse=True)
def node():
    """Generate an instance of a Node for testing"""
    node = Node((0, 0))
    yield node


def test_add_node(graph: Graph, node: Node):
    """Test that a node is correctly added to the graph."""
    graph.add_node(node)
    assert graph.size() == 1
    assert graph.node_count == 2


def test_map_edges(graph: Graph):
    """Test that edges are correctly mapped using the adjacency matrix."""
    nodes = [Node((0, 0)), Node((0, 1)), Node((0, 2)), Node((0, 3))]

    adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {
        (0, 0): [(0, 1), (0, 2)],
        (0, 1): [(0, 3), (0, 2)],
        (0, 2): [(0, 0), (0, 0)],
        (0, 3): [(0, 1), (0, 2)],
    }

    for node in nodes:
        graph.add_node(node)

    graph.map_edges(adjacency_list)

    assert len(graph.level.edges([1])) == 2
