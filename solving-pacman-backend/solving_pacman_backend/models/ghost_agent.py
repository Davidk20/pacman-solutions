"""Collection of models representing the Ghosts."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.movement_types import MovementTypes


class BlinkyAgent(Agent):
    """Agent Representing Blinky."""

    def __init__(self):
        """Initialise the class."""
        super().__init__("Blinky", "Shadow", MovementTypes.CHASE, 21, 200)


class PinkyAgent(Agent):
    """Agent Representing Pinky."""

    def __init__(self):
        """Initialise the class."""
        super().__init__("Pinky", "Speedy", MovementTypes.HOMEBOUND, 22, 200)


class InkyAgent(Agent):
    """Agent Representing Inky."""

    def __init__(self):
        """Initialise the class."""
        super().__init__("Inky", "Bashful", MovementTypes.HOMEBOUND, 23, 200)


class ClydeAgent(Agent):
    """Agent Representing Clyde."""

    def __init__(self):
        """Initialise the class."""
        super().__init__("Clyde", "Pokey", MovementTypes.HOMEBOUND, 24, 200)
