class Fan:
    # Class Constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # Constructor
    def __init__(self, 
                 speed: int = 1, 
                 on: bool = False,
                 radius: float = 5.0,
                 color: str = 'blue'):
        # If your setter does any kind of valdation,
        # you should always use the setter throughout the class
        # instead of using the data field directly
        self.set_speed(speed)
        self.__on = on
        self.__radius = radius
        self.__color = color

    def get_speed(self) -> int:
        return self.__speed
    
    def set_speed(self, speed: int = 1) -> None:
        if (speed == Fan.SLOW) or (speed == Fan.MEDIUM) or (speed == Fan.FAST):
            self.__speed = speed
        else:
            print('ERROR: Speed options are 1 (Slow), 2 (Medium), '
            'or 3 (Fast)')
            print('Speed of fan was not changed.')

    # Sometimes you want more control over how a datafield is changed
    # instead of just allowing any value to be assigned to the data field.
    def turn_on(self) -> None:
        if not self.__on: self.__on == True

    def turn_off(self) -> None:
        if self.__on: self.__on == False

    # Boolean getters names typically start with is or has.
    def is_on(self) -> bool:
        return self.__on
    
    def get_radius(self) -> float:
        return self.__radius
    
    # No radius setter because once a fan is created, the radius
    # cannot be changed.

    def get_color(self) -> str:
        return self.__color
    
    def set_color(self, color:str = 'blue') -> None:
        self.__color = color

    def __str__(self) -> str:
        output = f'Fan: {{ speed = {self.__speed}, on = {self.__on}, radius = {self.__radius}, color = {self.__color} }}'
        
        return output