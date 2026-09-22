from birthday import Birthday
class Person:
    def __init__(self, name: str = "John Smith", age: int = 30,
        birthday: Birthday = Birthday(), fav_colors: list[str] = []):

        # strs and ints are immutable, so these simple data fields are OK.
        self.__name = name
        self.__age = age
        # The birthday class must be designed to be immutable.
        self.__birthday = birthday

        # The list of colors should be stored as a tuple
        self.__fav_colors = tuple(fav_colors)

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_birthday(self) -> Birthday:
        return self.__birthday

    def get_fav_colors(self) -> tuple[str]:
        return self.__fav_colors

    # Setters
    # def set_name(self, name: str) -> None:
    #     self.__name = name

    # def set_age(self, age: int) -> None:
    #     self.__age = age

    # def set_birthday(self, birthday: Birthday) -> None:
    #     self.__birthday = birthday

    # def set_fav_colors(self, fav_colors: list[str]) -> None:
    #     self.__fav_colors = fav_colors

    # String representation
    def __str__(self) -> str:
        return f"Name: {self.__name}\n" + \
               f"Age: {self.__age}\n"  + \
               f"Birthday: {self.__birthday}\n"  + \
               f"Favorite Colors: {', '.join(self.__fav_colors)}"
        