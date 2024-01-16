"""Tests for the `GameStateStore`."""
from solving_pacman_backend.models.game_state import GameState
from solving_pacman_backend.models.game_state_store import GameStateStore


def test_add_size():
    """Tests that adding a state correctly appends it to the store."""
    state_store = GameStateStore()
    state = GameState(1, [])
    state_store.add(state)
    assert len(state_store.get()) == 1


def test_add_ordering():
    """Tests that the add function correctly sorted states."""
    state_store = GameStateStore()
    state_1 = GameState(5, [])
    state_2 = GameState(6, [])
    state_3 = GameState(1, [])
    state_4 = GameState(2, [])
    for state in [state_1, state_2, state_3, state_4]:
        state_store.add(state)
    assert state_store.get() == [state_3, state_4, state_1, state_2]
