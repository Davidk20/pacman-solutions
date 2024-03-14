"""Model representing the agent for Pac-man."""
from solving_pacman_backend.exceptions import PacManDiedException
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.movement_types import MovementTypes
from solving_pacman_backend.models.pickups import Pickup
from solving_pacman_backend.models.pickups import PowerPellet


class PacmanAgent(Agent):
    """Model representing the agent for Pac-man."""

    def __init__(self, home_path: list[tuple[int, int]]):
        """
        Initialise the class.

        Parameters
        ----------
        `home_path` : `list[tuple[int, int]]`
            The agents's home path.
        """
        super().__init__("Pac-Man", "Player", MovementTypes.CUSTOM, home_path, 44)
        self.current_lives = 3
        """Store the number of lives the user agent has remaining."""
        self.energized = False
        """
        Store whether Pac-man is currently energized. This is true when the
        agent has consumed a Power Pellet and is then able to consume ghosts.
        """
        self.temp_ghost_counter = 0
        """
        Counter to store the number of ghosts that Pac-man has consumed during
        a single energizer run
        """

    def __repr__(self) -> str:
        return (
            f"(Name: {self.name()}, Current Score: {self.score()},"
            f" Lives: {self.current_lives}, Energized: {self.energized}, "
            f"Ghosts Consumed: {self.temp_ghost_counter})"
        )

    def increase_score(self, score: int) -> None:
        """
        Increase the agents score.

        Parameters
        ----------
        `score` : `int`
            The amount of score to increase the Pac-Man's score by.
        """
        self._score += score

    def handle_consume(self, pickup: Pickup | Agent):
        """
        Handle the logic behind Pac-man consuming an item.

        :param pickup: The Pickup they have consumed.
        """
        if isinstance(pickup, PowerPellet):
            self.energized = True
        if isinstance(pickup, Agent):
            if self.energized:
                # If Pac-man has successfully consumed a ghost
                self.temp_ghost_counter += 1
                score = int(((pickup.score() / 100) ** self.temp_ghost_counter) * 100)
                self.increase_score(score)
            else:
                # If Pac-man has consumed a ghost without energizer
                self.current_lives -= 1
                raise PacManDiedException()
        if not isinstance(pickup, Agent):
            self.increase_score(pickup.score())

    def deenergize(self):
        """Restore Pac-man agent to a de-energized state."""
        self.energized = False
        self.temp_ghost_counter = 0

    def _perceive(self, time: int, level: list[list[int]]) -> None:
        raise NotImplementedError

    def _execute(self):
        raise NotImplementedError
