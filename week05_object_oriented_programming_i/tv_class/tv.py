
class TV:
    def __init__(self, channel: int = 1, volume_level: int = 1, on: bool = False):
        self.__channel: int = channel
        self.__volume_level: int = volume_level
        self.__on: bool = on

    def get_channel(self) -> int:
        return self.__channel

    def get_volume_level(self) -> int:
        return self.__volume_level

    def turn_on(self) -> None:
        self.__on = True

    def turn_off(self) -> None:
        self.__on = False
    
    def set_channel(self, channel:int=1) -> None:
        self.__channel = channel

    def set_volume(self, volume_level:int=1) -> None:
        if self.__on and volume_level >= 1 and volume_level <=7:
            self.__volume_level = volume_level

    def channel_up(self) -> None:
        if self.__on and self.__channel < 120:
            self.__channel += 1

    def channel_down(self) -> None:
        if self.__on and self.__channel > 1:
            self.__channel -= 1

    def volume_up(self) -> None:
        if self.__on and self.__volume_level < 7:
            self.__volume_level += 1

    def volume_down(self) -> None:
        if self.__on and self.__volume_level > 1:
            self.__volume_level -= 1