# Inheritance in Python is a fundamental concept in object-oriented programming that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and establishes a hierarchical relationship between classes.

class Parent:
    def greet(self):
        return "Hello from the Parent!"

class Child(Parent):
    def hello(self):
        return "Hello from the Child!"

child_instance = Child()
print(child_instance.greet())  # Output: Hello from the Parent!

parent_instance = Parent()
print(parent_instance.greet())



# Multiple Inheritance: A child class inherits from multiple parent classes.
class Parent1:
    def greet(self):
        return "Hello from Parent1!"

class Parent2:
    def farewell(self):
        return "Goodbye from Parent2!"

class Child(Parent1, Parent2):
    def hello(self):
        return "Hello from the Child!"

child_instance = Child()
print(child_instance.greet())   # Output: Hello from Parent1!
print(child_instance.farewell()) # Output: Goodbye from Parent2!


#Multilevel  Inheritance: A child class inherits from a parent class, which is also a child of another parent class.
class Grandparent:
    def greet(self):
        return "Hello from the Grandparent!"

class Parent(Grandparent):
    def hello(self):
        return "Hello from the Parent!"

class Child(Parent):
    def hi(self):
        return "Hello from the Child!"

child_instance = Child()
print(child_instance.greet())  # Output: Hello from the Grandparent!


#Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
class Parent:
    def greet(self):
        return "Hello from the Parent!"

class Child1(Parent):
    def hello(self):
        return "Hello from Child1!"

class Child2(Parent):
    def hi(self):
        return "Hello from Child2!"

child1_instance = Child1()
child2_instance = Child2()
print(child1_instance.greet())  # Output: Hello from the Parent!
print(child2_instance.greet())  # Output: Hello from the Parent!


# Overriding Methods -A child class can override methods from the parent class to provide specific implementation.
class Parent:
    def greet(self):
        return "Hello from the Parent!"

class Child(Parent):
    def greet(self) -> object:  # Overriding
        return "Hello from the Child!"

child_instance = Child()
print(child_instance.greet())  # Output: Hello from the Child!


