"""Tests for the Position class."""
from solving_pacman_backend.models.position import Position


def test_distance():
    """
    Test that distance is correctly calculated.

    As floats should not be compared directly, comparison is made
    by checking the difference is within a tolerable range.
    """
    p1 = Position(1, 1)
    p2 = Position(4, 7)
    assert p1.distance(p2) - 6.7082 <= 0.0001
