"""Model representing the agent for Pac-man."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.ghost_agent import GhostAgent
from solving_pacman_backend.models.pickups import Pickup
from solving_pacman_backend.models.pickups import PowerPellet


class PacmanAgent(Agent):
    """Model representing the agent for Pac-man."""

    def __init__(self):
        """Initialise the class."""
        super().__init__()
        self.current_score = 0
        """Store the current score the user agent has accumulated."""
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

    def handle_consume(self, pickup: Pickup | GhostAgent):
        """
        Handle the logic behind Pac-man consuming an item.

        :param pickup: The Pickup they have consumed.
        """
        if isinstance(pickup, PowerPellet):
            self.energized = True
        if isinstance(pickup, GhostAgent):
            if self.energized:
                # If Pac-man has successfully consumed a ghost
                self.temp_ghost_counter += 1
                self.current_score += (
                    (pickup.get_score() / 100) ** self.temp_ghost_counter
                ) * 100
            else:
                # If Pac-man has consumed a ghost without energizer
                self.current_lives -= 1
                # TODO - Return some sort of notification that this was invalid
        if not isinstance(pickup, GhostAgent):
            self.current_score += pickup.get_score()

    def get_score(self) -> int:
        """Return the current score."""
        return self.current_score

    def deenergize(self):
        """Restore Pac-man agent to a de-energized state."""
        self.energized = False
        self.temp_ghost_counter = 0
