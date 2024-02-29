"""Centralised file for all exceptions."""
##########################################
#            Level Exceptions
##########################################


class LevelNotFoundException(Exception):
    """Raised when a level is not found."""

    def __init__(self, level_num: int) -> None:
        super().__init__(f"Level {level_num} not found.")


class InvalidLevelConfigurationException(Exception):
    """Raised when a level is not configured correctly."""

    def __init__(self, level_num: int) -> None:
        super().__init__(f"Level {level_num} is not configured correctly.")


##########################################
#            Graph Exceptions
##########################################
class NodeNotFoundException(Exception):
    """Raised when a queried Node cannot be found."""

    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__(f"Node not found at {pos}.")


class DuplicateNodeException(Exception):
    """Raised when it is attempted to add a repeated node."""

    def __init__(self, node: str) -> None:
        super().__init__(f"{node} already in graph.")


class InvalidGraphConfigurationException(Exception):
    """Raised when the graph does not fit the required configuration."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NonAgentException(Exception):
    """Raised when there is an attempt to move a non-agent."""

    def __init__(self, entity: str) -> None:
        super().__init__(f"Type {entity} is not moveable.")
