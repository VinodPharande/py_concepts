"""
Polymorphism:
- Polymorphism is the ability to use a common interface for multiple forms (data types).
- In Python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
- In the example below, the animal_sound() function takes an object of the Animal class and calls the speak() method on it.
- The speak() method is defined in both the Cat and Lion classes.
- When we call the animal_sound() function with an object of the Cat class, the speak() method of the Cat class is called.
- Similarly, when we call the animal_sound() function with an object of the Lion class, the speak() method of the Lion class is called.

Key Points:
- Polymorphism means "many forms." It allows objects of different classes to be treated as objects of a common type.
- In Python, polymorphism is often implemented through method overriding (where a subclass provides a different 
implementation of a method inherited from its superclass) and "duck typing" (where an object's suitability is 
determined by its methods and attributes, not its type).
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):  # Method overriding
        print(f"{self.name}: Meow!")

class Lion(Animal):
    def speak(self):
        print(f"{self.name}: Roar!")

def animal_sound(animal):
    animal.speak()

my_lion = Lion("Simba")
my_cat = Cat("Whiskers")
animal_sound(my_cat) # Meow!
animal_sound(my_lion) # Roar!
