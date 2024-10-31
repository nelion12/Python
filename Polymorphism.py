#Polymorphism is a core concept in object-oriented programming (OOP) that allows methods to do different things based on the object or class invoking them. In Python, polymorphism is typically achieved through method overriding and operator overloading.

#Types of Polymorphism in Python
#Method Overriding: This occurs when a child class provides a specific implementation of a method that is already defined in its parent class. The child class method has the same name and parameters as the parent class method.
#Operator Overloading: This allows the same operator to have different meanings based on the context (usually involving different data types).

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Woof!"

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "Meow!"

# Instances of Dog and Cat
dog = Dog()
cat = Cat()

# Demonstrating polymorphism
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

# Using Polymorphism with a Common Interface
# You can also demonstrate polymorphism by using a common interface (method) to interact with different classes:

def animal_sound(animal):
    print(animal.speak())

# Using the function with different animal types
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

#Operator Overloading
#You can define how operators work with user-defined classes by overloading them:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading the + operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # String representation for easy printing
        return f"Point({self.x}, {self.y})"

# Creating instances of Point
point1 = Point(1, 2)
point2 = Point(3, 4)

# Using the overloaded + operator
point3 = point1 + point2

print(point3)  # Output: Point(4, 6)

#Summary
#Polymorphism allows methods and operators to function differently based on the context.
#Method Overriding allows child classes to provide specific implementations of methods defined in parent classes.
#Operator Overloading lets you define custom behavior for operators with user-defined classes.
#Polymorphism enhances code flexibility and allows for more generalized functions that can work with different types of objects! If you have further questions or need examples, feel free to ask!







