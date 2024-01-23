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
    """Abstract class used to provide core functionality to all agents."""

    def __init__(
        self,
        name: str,
        behaviour: str,
        movement_type: MovementTypes,
        value: int,
        score: int = 0,
    ):
        """
        Initialise the class.

        Parameters
        ----------
        `name` : `str`
            The name of the agent.
        `behaviour` : `str`
            The agents behaviour.
        `movement_type` : `MovementTypes`
            The agent's movement behaviours.
        `value` : `int`
            The agent's representation within the array.
        `score` : `int` : `default = 0`
            The score of the agent. Only ghost agents should override the
            score attribute as they have a score for `Pac-Man` to collect.
        """
        self.name = name
        """The name descriptor for the `Agent`."""
        self.behaviour = behaviour
        """The agent's behaviour."""
        self.movement_type = movement_type
        """The agents Movement type"""
        self.value = value
        """The value held by this item in the Array representation."""
        self.score = score
        """The score held by this agent."""

    def __repr__(self) -> str:
        return (
            f"(Name: {self.name}, Score: {self.score}, "
            f"Behaviour: {self.behaviour}, "
            f"Movement: {self.movement_type})"
        )

    def get_score(self) -> int:
        """
        Return the score for this agent.

        Returns
        -------
        The agents score.
        """
        return self.score

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
