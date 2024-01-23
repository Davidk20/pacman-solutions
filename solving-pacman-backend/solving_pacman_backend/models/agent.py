"""
Abstract class used to encapsulate all agent attributes.

Inspiration for this Agent model is being taken from the CS3940 Intelligent
Agents VacuumWorld abstraction. The core functionality of an `Agent` should
follow the agent cycle:

1) Perceive environment state and generate percept through `see()`
2) Revise internal state through `next()`
3) decide which action to select through `action()`
4) Return the action to be executed by the body

https://github.com/dicelab-rhul/vacuumworld
"""
from abc import ABC
from abc import abstractmethod

from solving_pacman_backend.models.movement_types import MovementTypes


class Agent(ABC):
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

    @abstractmethod
    def perceive(self) -> None:
        """Perceive the environment and generate perceptions."""
        raise NotImplementedError

    @abstractmethod
    def revise(self) -> None:
        """Revise internal states using the perceptions."""
        raise NotImplementedError

    @abstractmethod
    def execute(self) -> tuple[int, int]:
        """
        Returns the position which the `Agent` should move to.

        Uses the perceptions and revisions to decide the best action to take.

        Returns
        -------
        A `tuple` containing the coordinates for the agent to move to.
        """
        raise NotImplementedError
