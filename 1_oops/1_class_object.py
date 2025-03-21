# 
"""
Class and Object:
- Class is a blueprint for creating objects.
- An object is an instance of a class.
- A class defines the attributes and methods common to all objects of a certain kind.
- An object is a specific instance of a class.
- Objects can have unique attributes and methods.
- Classes and objects are fundamental concepts in object-oriented programming (OOP).

Key Points:
Classes:
    - A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that objects of that class will have.   
    - Think of it as a design for a type of object.
Objects:
    - An object is an instance of a class. It's a concrete realization of the class's blueprint.
    - Each object has its own unique set of attributes and can perform the methods defined in its class.
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever")  # Creating an object
print(my_dog.name)  # Accessing an attribute
my_dog.bark()  # Calling a method
