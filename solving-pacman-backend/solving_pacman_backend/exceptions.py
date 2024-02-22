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
