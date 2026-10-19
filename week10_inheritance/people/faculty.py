from person import Person

class Faculty(Person):
    def __init__(self, name, age, hair_color, salary):
        super().__init__(name, age, hair_color)

        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def __str__(self):
        output = super().__str__() + '\n'
        output += f'Salary: {self.__salary}'

        return output