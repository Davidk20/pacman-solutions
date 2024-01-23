"""Tests for the Ghost Agent."""
from random import choice

import pytest
from solving_pacman_backend.models import ghost_agent


@pytest.fixture(autouse=True)
def ghost():
    """Generate an agent of a Ghost which can be used for testing."""
    ghosts = [
        ghost_agent.BlinkyAgent(),
        ghost_agent.ClydeAgent(),
        ghost_agent.InkyAgent(),
        ghost_agent.PinkyAgent(),
    ]
    yield choice(ghosts)
