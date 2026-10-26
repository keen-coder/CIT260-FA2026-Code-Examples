// Parent class
abstract class Animal {
    public abstract void speak();
}

// Subclasses
class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Dog says Bark!");
    }
}

class Cat extends Animal {
    @Override
    public void speak() {
        System.out.println("Cat says Meow!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal a1 = new Dog();
        Animal a2 = new Cat();

        a1.speak();   // Dog says Bark!
        a2.speak();   // Cat says Meow!

        List<Animal> animals = new List<Animal>()

        animals.add(a1)
        animals.add(a2)

        for (i = 0 ; i < animals.size() ; i++) {
            animals.get(i).speak()
        }
    }
}