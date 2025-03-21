"""
Abstraction (using an abstract base class):
- Abstraction is the process of hiding the implementation details of an object and showing only the essential features of the object.
- In Python, abstraction can be achieved by using abstract base classes (ABCs).
- An abstract base class is a class that cannot be instantiated and can contain one or more abstract methods.
- An abstract method is a method that is declared in the abstract base class but does not contain an implementation.
- Subclasses of the abstract base class must implement the abstract methods.
- Abstraction helps in reducing code complexity and increases code reusability.
- In the example below, the Shape class is an abstract base class with an abstract method area().
- The Circle and Square classes are subclasses of the Shape class and implement the area() method.
- The area() method calculates the area of the circle and square, respectively.
- The main program creates objects of the Circle and Square classes and calls the area() method on them.
- The area() method of the Circle class calculates the area of a circle, and the area() method of the Square class calculates the area of a square.

Key Points:
- Abstraction involves hiding complex implementation details and showing only the essential features of an object.
- It simplifies the interface and allows users to focus on what an object does rather than how it does it.
- Python achieves abstraction through abstract classes and interfaces.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

my_circle = Circle(5)
my_square = Square(4)

print(my_circle.area()) #output 78.5
print(my_square.area()) #output 16