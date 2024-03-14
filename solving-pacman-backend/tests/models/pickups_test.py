"""Tests for the pickups in the game."""
from solving_pacman_backend.models.pickups import Apple
from solving_pacman_backend.models.pickups import Bell
from solving_pacman_backend.models.pickups import Cherry
from solving_pacman_backend.models.pickups import Galaxian
from solving_pacman_backend.models.pickups import Key
from solving_pacman_backend.models.pickups import Melon
from solving_pacman_backend.models.pickups import Orange
from solving_pacman_backend.models.pickups import PacDot
from solving_pacman_backend.models.pickups import PowerPellet
from solving_pacman_backend.models.pickups import Strawberry


def test_get_score():
    """Tests that the items all have the correct score"""
    assert PacDot().score() == 10
    assert PowerPellet().score() == 50
    assert Cherry().score() == 100
    assert Strawberry().score() == 300
    assert Orange().score() == 500
    assert Apple().score() == 700
    assert Melon().score() == 1000
    assert Galaxian().score() == 2000
    assert Bell().score() == 3000
    assert Key().score() == 5000
