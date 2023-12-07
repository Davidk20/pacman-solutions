"""Abstract class used to encapsulate all agent attributes."""
from solving_pacman_backend.models.movement_types import MovementTypes


class Agent:
    """Abstract class used to encapsulate all agent attributes."""

    def __init__(self):
        """Initialise the class."""
        self.name = "Agent"
        """The name descriptor for the `Agent`."""
        self.movement_type = None
        """The agents Movement type"""
        self.value = 999
        """
        The value held by this item in the Array representation
        """

    def set_movement_type(self, move_type: MovementTypes):
        """
        Set the movement type for the agent.

        :param move_type: The new movement type.
        """
        self.movement_type = move_type

    def __repr__(self) -> str:
        return f"""(Name: {self.name}, Value: {self.value})"""
