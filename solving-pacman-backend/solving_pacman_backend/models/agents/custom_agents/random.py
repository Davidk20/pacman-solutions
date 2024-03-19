"""Model representing the randomised Pac-Man behaviour"""
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.path import Path


class RandomPacMan(PacmanAgent):
    """
    Model representing the random Pac-Man behaviour.

    In this model, Pac-Man will randomly choose a path.
    """

    def __init__(self, home_path: list[tuple[int, int]]):
        super().__init__(home_path)

    def _perceive(self, time: int, level: Graph) -> None:
        self.path: Path = Path([])
        self.target = [self.position]
        if self.position == self.target[0]:
            self.target.pop(0)
        if len(self.target) == 0:
            self.target.append(level.random_node().position)
        self.path = level.shortest_path_to(self.position, self.target[0])
        # remove current pos from path to prevent static glitch
        self.path.get_next_pos()

    def _execute(self) -> tuple[int, int]:
        return self.path.get_next_pos().position
