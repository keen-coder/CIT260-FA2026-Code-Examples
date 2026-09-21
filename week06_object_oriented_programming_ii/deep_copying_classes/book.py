class Book:
    """
    Represents a book in a library.

    A Book object stores information about a book's
    title and author. This class is intentionally
    mutable because the title can be changed after
    the object is created.
    """

    def __init__(self, title: str, author: str):
        """
        Initializes a Book object.

        Args:
            title: The title of the book.
            author: The name of the author.
        """
        self.__title = title
        self.__author = author

    def get_title(self) -> str:
        """
        Returns the book's title.

        Returns:
            The title of the book.
        """
        return self.__title

    def get_author(self) -> str:
        """
        Returns the book's author.

        Returns:
            The author's name.
        """
        return self.__author

    def set_title(self, title: str) -> None:
        """
        Updates the book's title.

        Args:
            title: The new title.
        """
        self.__title = title

    def __str__(self) -> str:
        """
        Returns a string representation of the book.

        Returns:
            A string containing the title and author.
        """
        return f'"{self.__title}" by {self.__author}'

    def __repr__(self) -> str:
        return self.__str__()