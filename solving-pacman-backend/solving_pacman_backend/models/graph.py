"""Model representing the level as a graph data structure."""
import random
from typing import Type

from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.environment import EnvironmentEntity
from solving_pacman_backend.models.environment import Teleporter
from solving_pacman_backend.models.node import Node
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.pacman_agent import PacManDiedException
from solving_pacman_backend.models.path import Path
from solving_pacman_backend.models.pickups import Empty
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


class NonAgentException(Exception):
    """Raised when there is an attempt to move a non-agent."""

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

    def move_agent(self, old_pos: tuple[int, int], new_pos: tuple[int, int]) -> None:
        """
        Move an agent to the new position.

        It is assumed that the move has already been validated before being passed
        to the graph, as agents should only be able to move a distance of one node
        per move.

        Parameters
        ----------
        `old_pos` : `tuple[int, int]`
            The current position of the agent.
        `new_pos` : `tuple[int, int]`
            The position the agent is moving to.

        """
        new_node = self.find_node_by_pos(new_pos)
        old_node = self.find_node_by_pos(old_pos)
        if not isinstance(old_node.entity, Agent):
            # If non-agent attempts to move, raise and break.
            raise NonAgentException(f"Type {old_node.entity.name} is not moveable.")
        try:
            if isinstance(new_node.entity, (Agent, Pickup)):
                # pass collisions through to PacmanAgent to handle
                if isinstance(old_node.entity, PacmanAgent):
                    old_node.entity.handle_consume(new_node.entity)
            elif isinstance(new_node.entity, PacmanAgent) and isinstance(
                old_node.entity, Agent
            ):
                # Handle when a ghost collides with Pac-Man
                new_node.entity.handle_consume(old_node.entity)
            new_node.entity = old_node.entity
            old_node.entity = Empty()
        except PacManDiedException:
            # TODO Handle correct death logic here
            pass

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
        self, entity: Type[Agent | Pickup | EnvironmentEntity]
    ) -> list[Node]:
        """
        Find all `Node` objects matching the type provided.

        Parameters
        ----------
        `entity` : Type[Agent | Pickup]
            The type of entity to search for.

        Returns
        -------
        A `List` containing all matching `Node` Objects.
        - If `item == Agent`, the list should only contain one value.
        """
        nodes = []
        for node in self.level.keys():
            if isinstance(node.entity, entity):
                nodes.append(node)
        if entity == Agent and len(nodes) > 1:
            raise InvalidGraphConfigurationException(
                f"Only one of type {entity} should be present."
            )
        elif len(nodes) == 0:
            raise InvalidGraphConfigurationException(
                f"No instances of {entity} could be found."
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
        portals = self.find_node_by_entity(Teleporter)
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

    def is_repeated_cycle(self, path: list[Node]) -> bool:
        """
        Checks whether there is a repeated cycle within the path.

        This is done by checking for two consecutive Nodes being repeated at
        any point within the path.

        Parameters
        ----------
        `path` : `list[Node]`
            The path to check for repetition.

        Returns
        -------
        `True` if there is a repeated cycle.
        """
        for i in range(len(path) - 1):
            pair = [path[i], path[i + 1]]
            print(pair)
            for j in range(i + 1, len(path) - 1):
                print(j)
                if [path[j], path[j + 1]] == pair:
                    return True
        return False

    def find_paths_between(
        self, start_pos: tuple[int, int], end_pos: tuple[int, int]
    ) -> list[Path]:
        """
        Find all valid paths between two points.

        This function uses a iterative Depth-First Search algorithm to
        find all of the valid paths between the start and goal nodes. An iterative
        approach was taken over recursion because the graphs used for the levels
        are very complex and therefore could risk a RecursionError.

        This function will find and return ALL paths available. It is up
        to the agents internal decision making to decide which paths are to be
        kept and which are to be pruned. This is because all agents will have a
        different set of criteria for what constitutes a valid path.

        Parameters
        ----------
        `start_pos` : `tuple[int, int]`
            The starting position.
        `end_pos` : `tuple[int, int]`
            The goal position.

        Returns
        -------
        A `list` containing paths of `Node`'s.
        """
        # collect the nodes early so that error raised if they don't exist.
        start_node = self.find_node_by_pos(start_pos)
        end_node = self.find_node_by_pos(end_pos)
        # if the goal node is already found, return
        if start_node == end_node:
            return [Path([start_node])]
        # stack stores tuples of the start node and the path taken
        stack = [(start_node, [start_node])]
        paths = []
        while len(stack) > 0:
            current, path = stack.pop()
            if current == end_node:
                # once goal is reached, add path to paths
                paths.append(Path(path))
                continue
            for node in self.level[current]:
                # expand in all directions from current
                if node not in path:
                    # adds an updated path back into the stack
                    stack.append((node, path + [node]))
        return paths
