"""Tests for the GameState model."""
from solving_pacman_backend.models.game_state import GameState


def test_timer_increment():
    """Test that the timer correctly increments."""
    gameState = GameState()
    gameState.increment_timer()
    assert gameState.timer == 1
