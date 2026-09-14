
# Class Definition
class Rectangle:

    # Constructor definition
    def __init__(self, 
                 width: float = 1.0, 
                 height: float = 1.0) -> Rectangle:
        
        self.__width: float = width
        self.__height: float = height

    def get_width(self) -> float:
        return self.__width
    
    def set_width(self, width: float) -> None:
        self.__width = width
    
    def get_height(self) -> float:
        return self.__height

    def set_height(self, height: float) -> None:
        self.__height = height

    def perimeter(self) -> float:
        perimeter = (self.get_height() * 2) + (self.get_width() * 2)
        return perimeter
    
    def area(self) -> float:
        area = self.get_width() * self.get_height()
        return area

    def __str__(self: Rectangle) -> str:
        output: str = f'Rectangle:\n' \
                      f'\tHeight:\t\t{self.get_height()}\n' \
                      f'\tWidth:\t\t{self.get_width()}\n' \
                      f'\tPerimeter:\t{self.perimeter()}\n' \
                      f'\tArea:\t\t{self.area()}'
        
        return output
        
