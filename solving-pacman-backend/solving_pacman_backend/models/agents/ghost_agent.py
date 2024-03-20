"""Collection of models representing the Ghosts."""
from solving_pacman_backend.models import environment
from solving_pacman_backend.models.agents.agent import Agent
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.movement_types import MovementTypes
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
        self._internal_time: int = 0
        """
        The ghost's internal clock, not linked to game time.

        The ghost uses an internal timer to time its behaviour changes. This
        is required as, when frightened, the ghosts behaviours stop fluctuating
        between chase and scatter and should return to their pre-frightened
        state after the frightened timer expires
        """
        self.path: Path = Path([])
        """The path the agent is taking."""

    def _perceive(self, time: int, level: Graph) -> None:
        # Update behaviours
        if (
            self.movement_type != MovementTypes.FRIGHTENED
            and self.movement_type != MovementTypes.HOMEBOUND
        ):
            # Only update time when not frightened
            self._internal_time += 1

            if self._internal_time >= 20 and self._internal_time < 27:
                self.movement_type = MovementTypes.SCATTER
                # When scattering to home, this should become their target.
                self.target = self.home_path
            else:
                self.movement_type = MovementTypes.CHASE
                # Reset timer
                self._internal_time = 0

        pacman_node = level.find_node_by_entity(PacmanAgent)[0]
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

    def _perceive(self, time: int, level: Graph) -> None:
        super()._perceive(time, level)


class PinkyAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Pinky", "Speedy", MovementTypes.HOMEBOUND, homes, 22, 200)

    def _perceive(self, time: int, level: Graph) -> None:
        super()._perceive(time, level)
        return
        if level.total_pickups - level.remaining_pickups() == 1:
            self.movement_type = MovementTypes.CHASE
            self.path = Path([level.find_node_by_entity(environment.Gate)[0]])


class InkyAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Inky", "Bashful", MovementTypes.HOMEBOUND, homes, 23, 200)

    def _perceive(self, time: int, level: Graph) -> None:
        super()._perceive(time, level)
        return
        if level.total_pickups - level.remaining_pickups() == 30:
            self.movement_type = MovementTypes.CHASE
            self.path = Path([level.find_node_by_entity(environment.Gate)[0]])


class ClydeAgent(GhostAgent):
    def __init__(self, homes: list[tuple[int, int]]):
        super().__init__("Clyde", "Pokey", MovementTypes.HOMEBOUND, homes, 24, 200)

    def _perceive(self, time: int, level: Graph) -> None:
        super()._perceive(time, level)
        return
        if level.total_pickups - level.remaining_pickups() == 60:
            self.movement_type = MovementTypes.CHASE
            self.path = Path([level.find_node_by_entity(environment.Gate)[0]])
