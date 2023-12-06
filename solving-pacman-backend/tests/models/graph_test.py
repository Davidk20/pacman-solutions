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
    graph.add_node(node)
    assert len(graph.level.nodes) == 1
    assert graph.node_count == 2
