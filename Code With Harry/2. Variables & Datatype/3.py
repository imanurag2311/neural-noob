"""
Purpose: Use case of input function
Author: Anurag Yadav
Created: 27-07-2025
Language: Python (3.11.9)
Status: Final
"""


a = input("Enter your name: ")  # Input function to take user input
print("Hello, " + a)  # Print the input value with a greeting

b = input("Enter your age: ")  # Input function to take user input
print("You are " + b + " years old")  # Print the input value with age information

a = input("Enter number 1: ")
b = input("Enter number 2: ")
print ( a + b) # Concatenates the two input strings
# Note: Input values are treated as strings by default, so they are concatenated instead of added.


# To perform arithmetic operations:
a = int(input("Enter number 1: "))  # Convert input to integer -> We are use typecasting string here
b = int(input("Enter number 2: "))  # Convert input to integer
print(a + b)  # Prints the sum of the two integers

# Similarly, for other data types:
a = float(input("Enter number 1: "))  # Convert input to float
print(a)  # Prints the float value
b = bool(input("Enter true or false: "))  # Convert input to boolean
print(b)  # Prints the boolean value