"""Model representing the agent for Pac-man."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.pickups import Pickup


class PacmanAgent(Agent):
    """Model representing the agent for Pac-man."""

    def __init__(self):
        super().__init__()
        """Store the current score the user agent has accumulated."""
        self.current_score = 0
        """Store the number of lives the user agent has remaining."""
        self.current_lives = 3

    def increase_score(self, pickup: Pickup):
        """
        Add the score from the pickup to the agents game score.

        :param pickup: The Pickup they have consumed.
        """
        self.current_score += pickup.get_score()

    def get_score(self) -> int:
        """Return the current score."""
        return self.current_score
