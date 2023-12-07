"""Models representing the environment."""


class EnvironmentEntity:
    """Parent class representing a generic environment entity."""

    def __init__(self) -> None:
        """Initialise the class."""
        self.name = ""
        """The name descriptor for the `Pickup`."""
        self.value = 999
        """The value held by this item in the Array representation."""

    def __repr__(self) -> str:
        return f"""(Name: {self.name}, Value: {self.value})"""


class Wall(EnvironmentEntity):
    """Model representing a Wall."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Wall"
        self.value = 99


class Gate(EnvironmentEntity):
    """Model representing the gate between the ghost spawn and the map."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Gate"
        self.value = 20


class Teleporter(EnvironmentEntity):
    """Model representing the gate between teleporter locations."""

    def __init__(self) -> None:
        """Initialise the class."""
        super().__init__()
        self.name = "Teleporter"
        self.value = 88
