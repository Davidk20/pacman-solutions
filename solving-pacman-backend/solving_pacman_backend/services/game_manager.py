"""Service managing the running of the game."""
from solving_pacman_backend import exceptions
from solving_pacman_backend.exceptions import NonAgentException
from solving_pacman_backend.models import ghost_agent
from solving_pacman_backend.models.game_state import GameState
from solving_pacman_backend.models.game_state_store import GameStateStore
from solving_pacman_backend.models.graph import Graph
from solving_pacman_backend.models.pacman_agent import PacmanAgent
from solving_pacman_backend.models.placeholder_agent import PlaceholderAgent
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
        self.agent_home = level_handler.get_homes(level_num)
        """Dictionary containing the homes of the agents."""
        self.pacman = PacmanAgent(self.agent_home["pacman"])
        """Representation of the Pac-Man agent."""
        self.agents: list[PacmanAgent | ghost_agent.GhostAgent] = [
            self.pacman,
            ghost_agent.BlinkyAgent(self.agent_home["blinky"]),
            ghost_agent.PinkyAgent(self.agent_home["pinky"]),
            ghost_agent.InkyAgent(self.agent_home["inky"]),
            ghost_agent.ClydeAgent(self.agent_home["clyde"]),
        ]
        """Array containing all of the agents."""

    def setup_game(self) -> None:
        """
        Setup the game and board before the game starts.

        Injects the populated agents into the place of the dummy agents.
        """
        for placeholder in self.game.find_node_by_entity(PlaceholderAgent):
            for ag in self.agents:
                if placeholder.get_higher_entity().value() == ag.value():
                    placeholder.remove_entity(placeholder.get_higher_entity())
                    placeholder.add_entity(ag)
                    break

    def win(self) -> bool:
        """
        Checks whether the conditions for a win have been met.

        Returns
        -------
        `True` if the game is won and `False` otherwise.
        """
        return self.game.remaining_pickups() == 0

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
            try:
                ag.position = self.game.find_node_by_entity(type(ag))[0].position
                self.game.move_agent(ag.position, ag.cycle(self.timer, self.game))
            except exceptions.CollisionException as collision:
                if isinstance(
                    collision.agent, ghost_agent.GhostAgent
                ) and not isinstance(collision.colliding_entity, PacmanAgent):
                    # If the ghost collides with anything other than Pac-Man then ignore
                    return
                print(collision)
                if isinstance(collision.colliding_entity, PacmanAgent):
                    print("GAME OVER")
                    self.running = False

    def start(self) -> None:
        """Start the game loop."""
        self.running = True
        self.setup_game()
        while self.running:
            try:
                self.tick()
            except KeyboardInterrupt:
                print("\nSimulation manually stopped")
                self.print_current_state()
                break
            except NonAgentException as e:
                print(f"Error: {e}")
                self.print_current_state()
                break
        self.print_current_state()

    def print_current_state(self) -> None:
        """
        Print the latest state of the game.

        Used for debugging and should only be called when an exception is caught.
        """
        print(f"Iteration {self.timer}")
        print(level_utils.print_level(level_utils.graph_to_array(self.game)))


if __name__ == "__main__":
    # entry point to run a single game.
    game = GameManager(1)
    game.start()
