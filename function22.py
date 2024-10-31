def addtwonumber():
    num=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print(f"The sum of{num} and {num2} is {num+num2}")
    addtwonumber()

    # def add_two_numbers():
    #     # Get user input for the first number
    #     num = int(input("Enter the first number: "))
    #
    #     # Get user input for the second number
    #     num2 = int(input("Enter the second number: "))
    #
    #     # Print the sum of the two numbers
    #     print(f"The sum of {num} and {num2} is {num + num2}")
    #
    # # Call the function to execute it
    # add_two_numbers()

# person.py

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# If you want to run this file directly, you can include the following
if __name__ == "__main__":
    # Create instances of the Person class
    bridget = Person(name="Bridget", age=19, gender="Female")
    eliud = Person(name="Eliud", age=25, gender="Male")

    # Display the information for each person
    bridget.display_info()
    print()  # Add a newline for better readability
    eliud.display_info()



