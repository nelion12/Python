class Parent12:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Parent12):
    def greet(self):
        return f"My name is {self.name} and my age is {self.age} years old"


# Create an instance of Child
child_instance = Child(name="pesh", age=8)

# Call the greet method
print(child_instance.greet())  # Output: My name is pesh and my age is 8 years old
