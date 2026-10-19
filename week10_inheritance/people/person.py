
class Person:
    def __init__(self, name, age, hair_color):
        self._name = name
        self.set_age(age)
        self._hair_color = hair_color

    def set_age(self, age):
        if age < 0:
            raise ValueError()
        self.__age = age

    def get_name(self):
        return self.__name
    
    def __str__(self):
        output = f'Name: {self.__name}\n'
        output += f'Age: {self.__age}\n'
        output += f'Hair Color: {self.__hair_color}'

        return output