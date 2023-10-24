"""Collection of objects representing the pickups possible during gameplay."""


class Pickup:
    """Parent class representing a generic Pickup item"""

    def __init__(self) -> None:
        self.score = 0
        """
        The numerical value of the item which should be appended to the score
        when Pac-man consumes the item.
        """
        # TODO - When sprite sheets configured, create attribute for reference.

    def get_score(self) -> int:
        """Return the score for this item."""
        return self.score


class PacDot(Pickup):
    """Pickup class representing a standard Pac-Dot."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 10


class PowerPellet(Pickup):
    """Pickup class representing a Power Pellet, also known as an Energizer."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 50


class Cherry(Pickup):
    """Pickup class representing a Cherry."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 100


class Strawberry(Pickup):
    """Pickup class representing a Strawberry."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 300


class Orange(Pickup):
    """Pickup class representing a Orange."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 500


class Apple(Pickup):
    """Pickup class representing a Apple."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 700


class Melon(Pickup):
    """Pickup class representing a Melon."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 1000


class Galaxian(Pickup):
    """Pickup class representing a Galaxian."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 2000


class Bell(Pickup):
    """Pickup class representing a Bell."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 3000


class Key(Pickup):
    """Pickup class representing a Key."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 5000
