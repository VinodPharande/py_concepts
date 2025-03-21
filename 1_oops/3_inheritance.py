"""
Inheritance:
- Inheritance is a way to form new classes using classes that have already been defined. 
- The newly formed classes are called derived classes, the classes that we derive from are called base classes. 
- Important benefits of inheritance are code reuse and reduction of complexity of a program. 
- The derived classes (descendants) override or extend the functionality of base classes (ancestors).

Key Points:
- Inheritance allows a class (subclass or derived class) to inherit attributes and methods from another class (superclass or base class).   
- This promotes code reuse and creates a hierarchical relationship between classes.   
- Python supports single, multiple, and multilevel inheritance.
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

my_cat = Cat("Whiskers")
my_cat.speak() #output Meow!

my_lion = Lion("Simba")
my_lion.speak() #output Roar!