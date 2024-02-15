"""Service managing the running of the game."""
from solving_pacman_backend.models.game_state import GameState
from solving_pacman_backend.models.game_state_store import GameStateStore
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.services import level_handler
from solving_pacman_backend.utils import level_utils


class GameManager:
    """
    Service which manages the overall running of the game.
    """

    def __init__(self, level_num: int) -> None:
        """
        Initialises the `GameManager`.

        The game manager is responsible for building the game with all requirements
        and then running the game, managing its iteration and win / loss conditions.

        Parameters
        ----------
        `level_num` : `int`
            The number of the level to be run.
        """
        self.timer = 0
        """
        The internal game counter.

        A unit of time is interpreted as the duration it takes any agent to
        move one space anywhere on the board. This way, all movements take
        the same duration of time and can be counted within the same unit and
        the planner does not have to worry about moves being completed at
        different times and then having to factor this into collision
        calculations.
        """
        self.state_store = GameStateStore()
        """The store containing the history of the agents movements."""
        self.game: Graph = level_utils.array_to_graph(level_handler.get_map(level_num))
        """The graph containing the game."""
        self.running = False
        """Indicates whether the game is currently running."""
        self.pacman = PacmanAgent()
        """Representation of the Pac-Man agent."""

    def win(self) -> bool:
        """
        Checks whether the conditions for a win have been met.

        Returns
        -------
        `True` if the game is won and `False` otherwise.
        """
        return level_utils.remaining_pickups(self.game) == 0

    def lost(self) -> bool:
        """
        Checks whether the conditions for a loss have been met.

        Returns
        -------
        `True` if the game is lost and `False` otherwise.
        """
        return self.pacman.current_lives == 0

    def tick(self) -> None:
        """Increments the game time and processes all time based events."""
        level_array = level_utils.graph_to_array(self.game)
        self.state_store.add(GameState(self.timer, level_array))
        if self.win() or self.lost():
            self.running = False
        else:
            self.timer += 1
