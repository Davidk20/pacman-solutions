"""Collection of objects representing the pickups possible during gameplay."""


class Pickup:
    """Parent class representing a generic Pickup item."""

    def __init__(self) -> None:
        """Initialise the class."""
        self.name = "Pickup"
        """The name descriptor for the `Pickup`."""
        self.score = 0
        """
        The numerical value of the item which should be appended to the score
        when Pac-man consumes the item.
        """
        self.value = 999
        """
        The value held by this item in the Array representation
        """
        # TODO - When sprite sheets configured, create attribute for reference.

    def get_score(self) -> int:
        """Return the score for this item."""
        return self.score

    def __repr__(self) -> str:
        return f"""(Name: {self.name}, Score: {self.score}, Value: {self.value})"""


class Empty(Pickup):
    """`Pickup` class representing an empty space."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Empty"
        self.score = 0
        self.value = 0


class PacDot(Pickup):
    """Pickup class representing a standard Pac-Dot."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "PacDot"
        self.score = 10
        self.value = 1


class PowerPellet(Pickup):
    """Pickup class representing a Power Pellet, also known as an Energizer."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Power Pellet"
        self.score = 50
        self.value = 2


class Cherry(Pickup):
    """Pickup class representing a Cherry."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Cherry"
        self.score = 100
        self.value = 3


class Strawberry(Pickup):
    """Pickup class representing a Strawberry."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Strawberry"
        self.score = 300
        self.value = 4


class Orange(Pickup):
    """Pickup class representing a Orange."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Orange"
        self.score = 500
        self.value = 5


class Apple(Pickup):
    """Pickup class representing a Apple."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Apple"
        self.score = 700
        self.value = 6


class Melon(Pickup):
    """Pickup class representing a Melon."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Melon"
        self.score = 1000
        self.value = 7


class Galaxian(Pickup):
    """Pickup class representing a Galaxian."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Galaxian"
        self.score = 2000
        self.value = 8


class Bell(Pickup):
    """Pickup class representing a Bell."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Bell"
        self.score = 3000
        self.value = 9


class Key(Pickup):
    """Pickup class representing a Key."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Key"
        self.score = 5000
        self.value = 10
