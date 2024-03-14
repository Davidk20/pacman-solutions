from solving_pacman_backend.models import pickups
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.node import Node


class Path:
    """
    Model representing a single path.

    This object should be read-only, and acts as a wrapper to allow
    functions to take place on `Path`'s.
    """

    def __init__(self, path: list[Node]) -> None:
        self.route = path

    def __repr__(self) -> str:
        return f"Path from {self.route[0].position} to {self.route[-1].position}"

    def __len__(self) -> int:
        return len(self.route)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Path) or len(self.route) != len(__value):
            return False
        for a, b in zip(self.route, __value.route):
            if a != b:
                return False
        return True

    def is_safe(self) -> bool:
        """
        Checks whether a path is safe.

        Returns
        -------
        `True` if there are no Ghosts on a path.
        """
        return all(not isinstance(node.entity, Agent) for node in self.route)

    def cost(self) -> int:
        """
        Calculates the reward cost of the path.

        This value is seen as the reward for travelling down this path
        and is based on the sum of all score obtained should the agent
        successfully make it to the end of this path.
        """
        score = 0
        for node in self.route:
            if isinstance(node.entity, pickups.Pickup):
                score += node.entity.score()
        return score

    def get_next_pos(self) -> Node:
        """
        Returns the next position to move to and removes this from the queue.

        Returns
        -------
        The `Node` corresponding to the next target position.
        """
        return self.route.pop(0)
