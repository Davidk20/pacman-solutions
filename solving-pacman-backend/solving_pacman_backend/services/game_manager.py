"""Service managing the running of the game."""
from solving_pacman_backend.models import agent
from solving_pacman_backend.models import ghost_agent
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
        self.agent_home = {
            "Pac-Man": level_handler.get_home(level_num, "Pac-Man"),
            "Blinky": level_handler.get_home(level_num, "Blinky"),
            "Pinky": level_handler.get_home(level_num, "Pinky"),
            "Inky": level_handler.get_home(level_num, "Inky"),
            "Clyde": level_handler.get_home(level_num, "Clyde"),
        }
        """Dictionary containing the homes of the agents."""
        self.pacman = PacmanAgent(self.agent_home["Pac-Man"])
        """Representation of the Pac-Man agent."""
        self.blinky = ghost_agent.BlinkyAgent(self.agent_home["Blinky"])
        """Representation of the Blinky agent."""
        self.pinky = ghost_agent.PinkyAgent(self.agent_home["Pinky"])
        """Representation of the Pinky agent."""
        self.inky = ghost_agent.InkyAgent(self.agent_home["Inky"])
        """Representation of the Inky agent."""
        self.clyde = ghost_agent.ClydeAgent(self.agent_home["Clyde"])
        """Representation of the Clyde agent."""
        self.agents: list[agent.Agent] = [
            self.pacman,
            self.blinky,
            self.pinky,
            self.inky,
            self.clyde,
        ]
        """Array containing all of the agents."""

    def setup_game(self) -> None:
        """
        Setup the game and board before the game starts.

        Injects the populated agents into the place of the dummy agents.
        """
        for ag in self.agents:
            self.game.find_node_by_entity(type(ag))[0].entity = ag
            ag.position = self.game.find_node_by_entity(type(ag))[0].position

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
        for ag in self.agents:
            self.game.move_agent(ag.position, ag.cycle(self.state_store.get()[0]))

    def start(self) -> None:
        """Start the game loop."""
        self.running = True
        self.setup_game()
        while self.running:
            self.tick()


if __name__ == "__main__":
    # entry point to run a single game.
    game = GameManager(1)
    game.start()
