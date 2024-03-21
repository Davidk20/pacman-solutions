import pytest
from solving_pacman_backend.models import environment
from solving_pacman_backend.models import pickups
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.utils import agent_utils
from tests.mocks.mock_agent_test import mock_ghost


@pytest.fixture(scope="function", autouse=True)
def graph():
    """
    Returns a fully-mapped graph.

    For use where testing this functionality is not required.
    """
    graph = Graph()
    nodes = [
        Node((0, 0), PacmanAgent([(0, 0)], (0, 0))),
        Node((0, 1), pickups.PacDot()),
        Node((0, 2), pickups.PowerPellet()),
        Node((0, 3), pickups.Empty()),
        Node((0, 4), environment.Teleporter()),
        Node((0, 5), environment.Teleporter()),
        Node((0, 6), mock_ghost()),
        Node((0, 7), pickups.PacDot()),
        Node((0, 8), pickups.PacDot()),
        Node((0, 9), pickups.PacDot()),
    ]
    adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {
        (0, 0): [(0, 1), (0, 2), (0, 6)],
        (0, 1): [(0, 3), (0, 5)],
        (0, 2): [(0, 1), (0, 4)],
        (0, 3): [(0, 1), (0, 0)],
        (0, 4): [(0, 1), (0, 5)],
        (0, 5): [(0, 3), (0, 2)],
        (0, 6): [(0, 1), (0, 4), (0, 7)],
        (0, 7): [(0, 8)],
        (0, 8): [(0, 9)],
        (0, 9): [(0, 6)],
    }

    for node in nodes:
        graph.add_node(node)

    graph.map_edges(adjacency_list)
    yield graph


def test_random_turn(graph: Graph):
    """Test that a random choice of turn can be obtained."""
    n1 = graph.find_node_by_pos((0, 2))
    actual = agent_utils.choose_random_turn(graph, n1)
    assert isinstance(actual, Node) and actual in graph.get_adjacent(n1)
