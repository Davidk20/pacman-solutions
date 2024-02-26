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
        self.path = path

    def __repr__(self) -> str:
        return f"Path from {self.path[0].position} to {self.path[-1].position}"

    def __len__(self) -> int:
        return len(self.path)

    def is_safe(self) -> bool:
        """
        Checks whether a path is safe.

        Returns
        -------
        `True` if there are no Ghosts on a path.
        """
        return all(not isinstance(node.entity, Agent) for node in self.path)

    def cost(self) -> int:
        """
        Calculates the reward cost of the path.

        This value is seen as the reward for travelling down this path
        and is based on the sum of all score obtained should the agent
        successfully make it to the end of this path.

        TODO need to establish how ghosts factor in without knowing if energised
        """
        score = 0
        for node in self.path:
            if isinstance(node.entity, pickups.Pickup):
                score += node.entity.score
        return score
