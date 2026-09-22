class Birthday:
    def __init__(self, month: int = 1, day: int = 1, year: int = 1970):
        self.__month = month
        self.__day = day
        self.__year = year

    # Getters
    def get_month(self) -> int:
        return self.__month

    def get_day(self) -> int:
        return self.__day

    def get_year(self) -> int:
        return self.__year

    # Setters
    # def set_month(self, month: int) -> None:
    #     self.__month = month

    # def set_day(self, day: int) -> None:
    #     self.__day = day

    # def set_year(self, year: int) -> None:
    #     self.__year = year

    # String representation
    def __str__(self) -> str:
        return f"{self.__month}/{self.__day}/{self.__year}"

    def __repr__(self):
        return self.__str__()