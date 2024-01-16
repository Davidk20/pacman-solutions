"""Model storing the state of the game at an instance in time."""


class GameState:
    """Model storing the state of the game at an instance in time."""

    def __init__(self, time: int, level: list[list[int]]):
        """
        Initialise a new game state snapshot.

        Parameters
        ----------
        `time` : `int`
            The time corresponding to the snapshot.
        `board_state` : `list[list[int]]`
            A snapshot of the board state at the time.
        """
        self.time = time
        """Stores the time corresponding to the snapshot."""
        self.board_state: list[list[int]] = level
        """Store the reference to the current board state."""
