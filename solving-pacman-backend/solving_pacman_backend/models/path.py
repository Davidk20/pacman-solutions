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
