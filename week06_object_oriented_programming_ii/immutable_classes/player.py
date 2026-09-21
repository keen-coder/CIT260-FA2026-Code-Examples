class Player:
    """
    Represents a player on a sports team.

    A Player object stores a player's jersey number
    and name. This class is intentionally mutable
    because the player's name can be changed after
    the object is created.
    """

    def __init__(self, number: int, name: str):
        """
        Initializes a Player object.

        Args:
            number: The player's jersey number.
            name: The player's name.
        """
        self.__number = number
        self.__name = name

    def get_number(self) -> int:
        """
        Returns the player's jersey number.

        Returns:
            The player's jersey number.
        """
        return self.__number

    def get_name(self) -> str:
        """
        Returns the player's name.

        Returns:
            The player's name.
        """
        return self.__name

    def set_name(self, name: str) -> None:
        """
        Updates the player's name.

        Args:
            name: The player's new name.
        """
        self.__name = name

    def __str__(self) -> str:
        """
        Returns a string representation of the player.

        Returns:
            The player's jersey number and name.
        """
        return f'#{self.__number} {self.__name}'
