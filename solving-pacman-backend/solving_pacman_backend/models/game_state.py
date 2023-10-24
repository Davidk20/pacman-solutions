"""Model storing the state of the game."""
from solving_pacman_backend.models.ghost_agent import BlinkyAgent
from solving_pacman_backend.models.ghost_agent import ClydeAgent
from solving_pacman_backend.models.ghost_agent import InkyAgent
from solving_pacman_backend.models.ghost_agent import PinkyAgent
from solving_pacman_backend.models.pacman_agent import PacmanAgent


class GameState:
    """Model storing the state of the game."""

    def __init__(self):
        """
        Initialise a new game state.

        Should be used at the start of a level attempt.
        """
        self.timer = 0
        """Store the internal game time counter."""
        # TODO - Add correct reference attribute to board state here.
        self.board_state = None
        """Store the reference to the current board state."""
        self.pacmanAgent = PacmanAgent()
        """Agent representing Pac-man."""
        self.blinkyAgent = BlinkyAgent()
        """Agent representing Blinky the Ghost."""
        self.pinkyAgent = PinkyAgent()
        """Agent representing Pinky the Ghost."""
        self.inkyAgent = InkyAgent()
        """Agent representing Inky the Ghost."""
        self.clydeAgent = ClydeAgent()
        """Agent representing Clyde the Ghost."""

    def increment_timer(self):
        """
        Increment the global time by one unit.

        A unit of time is interpreted as the duration it takes any agent to
        move one space anywhere on the board. This way, all movements take
        the same duration of time and can be counted within the same unit and
        the planner does not have to worry about moves being completed at
        different times and then having to factor this into collision
        calculations.
        """
        self.timer += 1
