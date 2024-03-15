"""Collection of models representing the Ghosts."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.movement_types import MovementTypes
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.path import Path


class GhostAgent(Agent):
    """
    Generic agent representing the behaviour of all 4 ghosts.

    Initially, all four ghosts will have the same behaviour and
    therefore can be represented by the same agent. In future
    iterations, they may be evolved to include the subtle differences
    that the ghosts exhibit and so they would be separated into the
    four separate classes again.
    """

    def __init__(
        self,
        name: str,
        behaviour: str,
        movement_type: MovementTypes,
        home_path: list[tuple[int, int]],
        value: int,
        score: int = 0,
    ):
        super().__init__(name, behaviour, movement_type, home_path, value, score)

    def _perceive(self, time: int, level: Graph) -> None:
        # When returning an agent it should return a single item
        pacman_node = level.find_node_by_entity(PacmanAgent)[0]
        self.path: Path = Path([])
        match self.movement_type:
            case MovementTypes.CHASE:
                # If chasing Pac-Man, this should be the only target.
                self.target = [pacman_node.position]
                self.path = level.shortest_path_to(self.position, self.target[0])
                # The path contains the current pos which must be popped from the list
                self.path.get_next_pos()
            case MovementTypes.SCATTER:
                # When scattering to home, this should become their target.
                self.target = self.home_path
            case _:
                # All other conditions should clear the target.
                self.target = []

    def _execute(self) -> tuple[int, int]:
        match self.movement_type:
            case MovementTypes.CHASE:
                return self.path.get_next_pos().position
            case _:
                return self.position


class BlinkyAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Blinky", "Shadow", MovementTypes.CHASE, homes, 21, 200)


class PinkyAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Pinky", "Speedy", MovementTypes.HOMEBOUND, homes, 22, 200)


class InkyAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Inky", "Bashful", MovementTypes.HOMEBOUND, homes, 23, 200)


class ClydeAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Clyde", "Pokey", MovementTypes.HOMEBOUND, homes, 24, 200)
