from solving_pacman_backend.models.node import Node


class Path:
    """Model representing a single path."""

    def __init__(self, path: list[Node]) -> None:
        self.path = path
