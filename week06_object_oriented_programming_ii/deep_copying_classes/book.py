class Book:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def set_title(self, title: str) -> None:
        self.__title = title

    def __str__(self) -> str:
        return f'"{self.__title}" by {self.__author}'