from person import Person

class Student(Person):

    def __init__(self, name, age, hair_color, classes):
        super().__init__(name, age, hair_color)
        self.__classes = classes

    def get_classes(self):
        return self.__classes
    
    def __str__(self):
        output = f'hair color: {self._hair_color}'



        output = super().__str__() + '\n'
        output += f'Classes: {self.__classes}'

        return output
        



