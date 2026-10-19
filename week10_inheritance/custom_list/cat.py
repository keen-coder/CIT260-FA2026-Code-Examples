
cat1 =  Cat()

cat1.name




class Cat:
    def __init__(self, name: str, age: int, color: str, gender: str, fur_length: str):
        self._name = name
        self.set_age(age)
        self.set_color(color)
        self.set_gender(gender)
        self.set_fur_length(fur_length)

    # ---- Name ----
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        if not isinstance(name, str) or name == '':
            raise ValueError("ERROR: Name must be a non-empty string")
        
        self.__name = name

    # ---- Age ----
    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if not isinstance(age, int) or age < 0:
            raise ValueError("ERROR: Age must be a non-negative integer")
        
        self.__age = age

    # ---- Color ----
    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str):
        if not isinstance(color, str) or color == '':
            raise ValueError("Color must be a non-empty string")
        
        self.__color = color

    # ---- Gender ----
    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str):
        # Make sure the gender is lowercase
        gender = gender.lower()
        
        if not isinstance(gender, str) or \
           (gender != 'male' and gender != 'female'):
            raise ValueError("ERROR: Gender must be 'male' or 'female'")
        
        self.__gender = gender

    # ---- Fur Length ----
    def get_fur_length(self) -> str:
        return self.__fur_length

    def set_fur_length(self, fur_length: str):
        if not isinstance(fur_length, str) or \
           fur_length != 'short' and \
           fur_length != 'medium' and \
           fur_length != 'long':

            raise ValueError("Invalid fur length")
        
        self.__fur_length = fur_length

    def __str__(self):
        output = f'Cat{{{self.__name}, {self.__age}, {self.__color}, {self.__gender}, {self.__fur_length}}}'
        return output
    
    # def __repr__(self):
    #     return self.__str__()
