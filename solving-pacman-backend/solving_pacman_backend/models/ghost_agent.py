"""Collection of models representing the Ghosts."""
from solving_pacman_backend.models.agent import Agent
from solving_pacman_backend.models.game_state import GameState
from solving_pacman_backend.models.movement_types import MovementTypes
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.path import Path
from solving_pacman_backend.utils import level_utils


class BlinkyAgent(Agent):
    """Agent Representing Blinky."""

    def __init__(self, home_path: list[tuple[int, int]]):
        """
        Initialise the class.

        Parameters
        ----------
        `home_path` : `list[tuple[int, int]]`
            The agents's home path.
        """
        super().__init__("Blinky", "Shadow", MovementTypes.CHASE, home_path, 21, 200)

    def _perceive(self, state: GameState) -> None:
        graph = level_utils.array_to_graph(state.board_state)
        # When returning an agent it should return a single item
        pacman_node = graph.find_node_by_entity(PacmanAgent)[0]
        self.path: Path = Path([])
        match self.movement_type:
            case MovementTypes.CHASE:
                # If chasing Pac-Man, this should be the only target.
                self.target = [pacman_node.position]
                self.path = graph.shortest_path_to(self.position, self.target[0])
                # The path contains the current pos which must be popped from the list
                self.path.get_next_pos()
                # print(self.path.route)
            case MovementTypes.SCATTER:
                # When scattering to home, this should become their target.
                self.target = self.home_path
            case _:
                # All other conditions should clear the target.
                self.target = []

    def _execute(self) -> tuple[int, int]:
        return self.path.get_next_pos().position


class PinkyAgent(Agent):
    """Agent Representing Pinky."""

    def __init__(self, home_path: list[tuple[int, int]]):
        """
        Initialise the class.

        Parameters
        ----------
        `home_path` : `list[tuple[int, int]]`
            The agents's home path.
        """
        super().__init__("Pinky", "Speedy", MovementTypes.HOMEBOUND, home_path, 22, 200)

    def _perceive(self, state: GameState) -> None:
        raise NotImplementedError

    def _execute(self):
        raise NotImplementedError


class InkyAgent(Agent):
    """Agent Representing Inky."""

    def __init__(self, home_path: list[tuple[int, int]]):
        """
        Initialise the class.

        Parameters
        ----------
        `home_path` : `list[tuple[int, int]]`
            The agents's home path.
        """
        super().__init__("Inky", "Bashful", MovementTypes.HOMEBOUND, home_path, 23, 200)

    def _perceive(self, state: GameState) -> None:
        raise NotImplementedError

    def _execute(self):
        raise NotImplementedError


class ClydeAgent(Agent):
    """Agent Representing Clyde."""

    def __init__(self, home_path: list[tuple[int, int]]):
        """
        Initialise the class.

        Parameters
        ----------
        `home_path` : `list[tuple[int, int]]`
            The agents's home path.
        """
        super().__init__("Clyde", "Pokey", MovementTypes.HOMEBOUND, home_path, 24, 200)

    def _perceive(self, state: GameState) -> None:
        raise NotImplementedError

    def _execute(self):
        raise NotImplementedError
