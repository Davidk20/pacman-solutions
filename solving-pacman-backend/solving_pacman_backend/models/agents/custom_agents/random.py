"""Model representing the randomised Pac-Man behaviour"""
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.utils.agent_utils import gen_random_path


class RandomPacMan(PacmanAgent):
    """
    Model representing the random Pac-Man behaviour.

    In this model, Pac-Man will randomly choose a path.
    """

    def __init__(self, home_path: list[tuple[int, int]]):
        super().__init__(home_path)

    def _perceive(self, time: int, level: Graph) -> None:
        # Remove target if agent has reached position
        if len(self.target) > 0 and self.position == self.target[0]:
            self.target.pop(0)
        # If there is no target, assign new target
        if len(self.target) == 0:
            self.target, self.path = gen_random_path(
                level, self.position, self.move_history
            )
        self.path.get_next_pos()

    def _execute(self) -> tuple[int, int]:
        move = self.path.get_next_pos().position
        self.move_history.append(move)
        return move
