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
    assert PacDot().get_score() == 10
    assert PowerPellet().get_score() == 50
    assert Cherry().get_score() == 100
    assert Strawberry().get_score() == 300
    assert Orange().get_score() == 500
    assert Apple().get_score() == 700
    assert Melon().get_score() == 1000
    assert Galaxian().get_score() == 2000
    assert Bell().get_score() == 3000
    assert Key().get_score() == 5000
