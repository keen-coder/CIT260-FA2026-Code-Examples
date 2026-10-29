class Animal:
    def speak(self):
        return NotImplementedError
    
class Dog(Animal):
    def speak(self):
        return 'Dog says Bark!'

class Cat(Animal):
    def speak(self):
        return 'Cat says Meow!'

class Chicken(Animal):
    def speak(self):
        return 'Chicken says Bawk!'

class Cow(Animal):
    def speak(self):
        return 'Cow says Mooo!'
    
def main():
    cat1 = Cat()
    dog1 = Dog()
    chicken1 = Chicken()
    cow1 = Cow()

    animals = [cat1, dog1, chicken1, cow1]

    for animal in animals:
        print(animal.speak())

def make_animals_speak(animals: list[Animal]):
    for animal in animals:
        print(animal.speak())


if __name__ == '__main__':
    main()