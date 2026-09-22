from book import Book
from copy import deepcopy

class Library:
    """
    Represents a library.
    """

    def __init__(self, name: str, books: list[Book]):
        self.__name = name
        self.__books = books

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name) -> None:
        self.__name = name

    def get_books(self) -> list[Book]:
        return self.__books

    def copy(self) -> Library:
       return deepcopy(self)

    def __str__(self):
        return f'Library: {self.__name}, {self.__books}'