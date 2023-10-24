"""Collection of models representing the Ghost agents."""
from solving_pacman_backend.models.agent import Agent


class GhostAgent(Agent):
    """Agent representing the parent type for all Ghosts."""

    def __init__(self):
        """Initialise the class."""
        super().__init__()
        self.name = ""
        """The name of the ghost."""
        self.behaviour = ""
        """The behaviour of the ghost."""
        self.score = 200
        """
        The base score for Pac-man to consume a ghost. This value is multiplied
        based on how many ghosts Pac-man can consume during a single Power
        Pellet run. The handling for this will be controlled by PacmanAgent.
        """
        self.current_movement_type = None
        """The current movement type of the Ghost."""

    def get_score(self) -> int:
        """Return the score for this item."""
        return self.score


class BlinkyAgent(GhostAgent):
    """Agent Representing Blinky the Ghost."""

    def __init__(self):
        """Initialise the class."""
        super().__init__()
        self.name = "Blinky"
        self.behaviour = "Shadow"


class PinkyAgent(GhostAgent):
    """Agent Representing Pinky the Ghost."""

    def __init__(self):
        """Initialise the class."""
        super().__init__()
        self.name = "Pinky"
        self.behaviour = "Speedy"


class InkyAgent(GhostAgent):
    """Agent Representing Inky the Ghost."""

    def __init__(self):
        """Initialise the class."""
        super().__init__()
        self.name = "Inky"
        self.behaviour = "Bashful"


class ClydeAgent(GhostAgent):
    """Agent Representing Clyde the Ghost."""

    def __init__(self):
        """Initialise the class."""
        super().__init__()
        self.name = "Clyde"
        self.behaviour = "Pokey"
