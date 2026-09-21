from player import Player

class Team:
    """
    Represents an immutable team.

    Once a Team object is created, its name and
    collection of players cannot be changed through
    the public interface.

    To help preserve immutability, the player list
    is converted to a tuple during construction.
    """

    def __init__(self, name: str, players: list[Player]):
        """
        Initializes a Team object.

        Args:
            name: The team's name.
            players: A list of Player objects on the team.
        """
        self.__name = name

        # Convert the list to an immutable tuple.
        self.__players = tuple(players)

    def get_name(self) -> str:
        """
        Returns the team's name.

        Returns:
            The team's name.
        """
        return self.__name

    def get_players(self) -> tuple[Player]:
        """
        Returns the players on the team.

        Returns:
            A tuple containing the team's players.
        """
        return self.__players

    def __str__(self) -> str:
        """
        Returns a string representation of the team.

        Returns:
            The team's name.
        """
        return f'Team Name: {self.__name}\n' \
               f'Players: {self.__players}'  