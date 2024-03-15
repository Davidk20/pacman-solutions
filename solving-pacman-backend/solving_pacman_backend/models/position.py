"""Model representing a position in two-dimensional space."""


class Position:
    """Model representing a position in two-dimensional space."""

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        """The x-coordinate."""
        self.y = y
        """The y-coordinate."""

    def distance(self, other) -> float:
        """
        Calculates the distance between this position and the `other` position
        using the Euclidean Distance.

        Parameters
        ----------
        `other` : `Position`
            The other position to calculate the distance to,
            rounded to 4 decimal places.
        """
        return round(((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5, 4)
