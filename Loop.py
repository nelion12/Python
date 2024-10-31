# while loop
#increament loop
# Initialize the starting value
num = 3

# Start the while loop
while num <= 15:
    print(f"loop: {num}")  # Print the current value
    num += 2               # Increment the value by 2

#decreasing loop
#create a while loop from 100/decreases by 5 to zero
# Initialize the starting value
value = 100

# Start the while loop
while value >= 0:
    print(value)  # Print the current value
    value -= 5    # Decrease the value by 5


    #for loop
    fruits=["mangoes","oranges","apples","watermelon"]

    for eliud in fruits:
        print(eliud)

numbers= [23, 1, 45, 34, 99, 4]
numbers.sort()
print(numbers)

numbers = [23, 1, 45, 34, 99, 4]

# Create a new sorted list from largest to smallest
sorted_numbers = sorted(numbers, reverse=True)

# Print the sorted list
print(sorted_numbers)
