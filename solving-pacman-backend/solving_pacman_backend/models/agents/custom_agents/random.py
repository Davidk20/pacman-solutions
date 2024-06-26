"""Model representing the randomised Pac-Man behaviour"""

from random import choice

from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.graph import Graph


class RandomPacMan(PacmanAgent):
    """
    Model representing the random Pac-Man behaviour.

    In this model, Pac-Man will randomly choose a path. I have chosen to
    implement this behaviour similar to that of a frightened ghost.
    Pac-Man will randomly choose a new direction at each junction.
    """

    def __init__(
        self, home_path: list[tuple[int, int]], respawn_point: tuple[int, int]
    ):
        super().__init__(home_path, respawn_point)

    def _perceive(self, time: int, level: Graph) -> None:
        all_paths = level.find_path_to_next_jct(self.position)
        # prune paths where the path only contains the target.
        valid_paths = [path for path in all_paths if len(path) > 2]
        self.path = choice(valid_paths)
        if self.path.route[0].position == self.position:
            # if the path contains the current pos it must be removed from the list
            self.path.get_next_pos()

    def _execute(self) -> tuple[int, int]:
        move = self.path.get_next_pos().position
        self.move_history.append(move)
        return move
