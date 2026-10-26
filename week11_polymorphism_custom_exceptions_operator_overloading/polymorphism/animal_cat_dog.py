class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return 'Dog says Bark!'

class Cat(Animal):
    def speak(self):
        return 'Cat says Meow!'

class Chicken(Animal):
    def speak(self):
        return 'Chicken says Bawk!'
    
def main():
    cat1 = Cat()
    dog1 = Dog()
    chicken1 = Chicken()

    animals = [cat1, dog1, chicken1]

    for animal in animals:
        print(animal.speak())

if __name__ == '__main__':
    main()