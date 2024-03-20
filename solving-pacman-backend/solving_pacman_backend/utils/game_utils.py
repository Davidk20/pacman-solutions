"""Utility functions to assist running the game."""
from solving_pacman_backend.models import environment
from solving_pacman_backend.models import pickups
from solving_pacman_backend.models.agents import ghost_agent
from solving_pacman_backend.models.agents.pacman_agent import PacmanAgent
from solving_pacman_backend.models.node import Node


def handle_collision(node: Node) -> None:
    higher = node.get_higher_entity()
    lower = node.get_lower_entity()

    if isinstance(lower, environment.Teleporter):
        # If passing through teleporter, ignore
        return

    # if ghost collides with anything but Pac-Man, ignore
    if node.contains(ghost_agent.GhostAgent) and not node.contains(PacmanAgent):
        return

    if isinstance(higher, PacmanAgent):
        pacman = higher
        if isinstance(lower, (pickups.Pickup, ghost_agent.GhostAgent)):
            pacman.handle_consume(lower)
        if isinstance(lower, pickups.Pickup):
            node.entities.remove(node.get_lower_entity())
    elif isinstance(higher, ghost_agent.GhostAgent) and isinstance(lower, PacmanAgent):
        pacman = lower
        pacman.handle_consume(higher)
    else:
        raise ValueError(f"Invalid case higher - {higher}, lower - {lower}")
