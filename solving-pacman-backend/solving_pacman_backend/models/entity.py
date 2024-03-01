"""Model representing all entities within the game."""


class Entity:
    def __init__(self, name: str, score: int = 0, value: int = 999) -> None:
        """
        Initialise an Entity.

        Parameters
        ----------
        `name` : `str`
            The name of the entity.
        `score` : `int`
            The score the entity has.
        `value` : `int`
            The agent's representation within the array.
        """
        self.name = name
        """The name of the entity."""
        self.score = score
        """The score the entity has."""
        self.value = value
        """The agent's representation within the array."""
