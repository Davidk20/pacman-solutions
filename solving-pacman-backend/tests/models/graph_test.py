import pytest
from solving_pacman_backend.models.graph import DuplicateNodeException
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.graph import NodeNotFoundException
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pickups import PacDot
from solving_pacman_backend.models.pickups import PowerPellet


@pytest.fixture(autouse=True)
def graph():
    """Generate an instance of Graph for testing"""
    graph = Graph()
    yield graph


@pytest.fixture(scope="session", autouse=True)
def node():
    """Generate an instance of a Node for testing"""
    node = Node((0, 0), PacDot())
    yield node


@pytest.fixture(scope="session", autouse=True)
def nodes():
    """Generate an list of a Node for testing"""
    nodes = [
        Node((0, 0), PacDot()),
        Node((0, 1), PacDot()),
        Node((0, 2), PowerPellet()),
        Node((0, 3), PacDot()),
    ]
    yield nodes


@pytest.fixture(scope="session", autouse=True)
def adjacency_list():
    """Generate the adjacency list for testing, uses `nodes`."""
    adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {
        (0, 0): [(0, 1), (0, 2)],
        (0, 1): [(0, 3), (0, 2)],
        (0, 2): [(0, 0), (0, 1)],
        (0, 3): [(0, 1), (0, 2)],
    }
    yield adjacency_list


def test_add_node(graph: Graph, node: Node):
    """Test that a node is correctly added to the graph."""
    graph.add_node(node)
    assert graph.num_of_nodes() == 1
    assert graph.node_count == 2


def test_add_repeated_node(graph: Graph, node: Node):
    """Test that exception is raised when duplicate node is added."""
    graph.add_node(node)
    with pytest.raises(DuplicateNodeException):
        graph.add_node(node)


def test_find_node_by_pos(graph: Graph, node: Node):
    """Test that a node can be found if it is in the graph."""
    graph.add_node(node)
    assert graph.find_node_by_pos((0, 0)) == node


def test_find_node_by_pos_raises(graph: Graph, node: Node):
    """Test that an error is raised if a node cannot be found when not in the graph."""
    graph.add_node(node)
    with pytest.raises(NodeNotFoundException):
        graph.find_node_by_pos((0, 1))


def test_find_by_entity(graph: Graph, nodes: list[Node]):
    """Test that a node can be found by searching for entity."""
    for node in nodes:
        graph.add_node(node)
    result = graph.find_node_by_entity(PowerPellet())
    assert result[0].entity.value == nodes[2].entity.value and len(result) == 1
