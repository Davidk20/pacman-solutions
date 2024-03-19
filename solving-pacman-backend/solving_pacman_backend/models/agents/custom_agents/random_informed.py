"""Model representing the informed randomised Pac-Man behaviour"""
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.graph import Graph


class RandomInformedPacMan(PacmanAgent):
    """
    Model representing the informed random Pac-Man behaviour.

    In this model, Pac-Man will randomly choose a path, however,
    should he reach an unsafe path, Pac-Man will randomly
    choose a new position as target.
    """

    def __init__(self, home_path: list[tuple[int, int]]):
        super().__init__(home_path)

    def _perceive(self, time: int, level: Graph) -> None:
        # Remove target if agent has reached position
        if len(self.target) > 0 and self.position == self.target[0]:
            self.target.pop(0)
        # If there is no target, assign new target
        if len(self.target) == 0:
            self.target.append(level.random_node().position)
        # Find path to target
        self.path = level.shortest_path_to(self.position, self.target[0])
        while not self.path.is_safe():
            # Looks for a new path every time the path is deemed unsafe.
            self.target[0] = level.random_node().position
            self.path = level.shortest_path_to(self.position, self.target[0])

        if len(self.move_history) > 0:
            # If the agent has a move history, check that the agent
            # is not moving backwards
            while self.path.backwards(self.move_history):
                self.target.pop(0)
                self.target.append(level.random_node().position)
                self.path = level.shortest_path_to(self.position, self.target[0])
        # remove current pos from path to prevent static glitch
        self.path.get_next_pos()

    def _execute(self) -> tuple[int, int]:
        move = self.path.get_next_pos().position
        self.move_history.append(move)
        return move
