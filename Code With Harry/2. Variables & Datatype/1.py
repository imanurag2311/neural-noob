"""
Purpose: Various types of data type and operations
Author: Anurag Yadav
Created: 27-07-2025
Language: Python (3.11.9)
Status: Final
"""

print("Types of variable")
a = 2 # a is integer
b = 23.66 # b is float
c = "Anurag" # c is string
d = True # d is boolean
e = None # Non type variable data type, to mark nothing

print(a, b, c, d, e) # use to print multiple variables

""" 
   RULES FOR CHOOSING AN IDENTIFIER
        1. A variable name can contain alphabets, digits, and underscores.
        2. A variable name can only start with an alphabet and underscores.
        3. A variable name can’t start with a digit.
        4. No while space is allowed to be used inside a variable name.
"""

# Performing various oprations on variables

# Arithmetic operations
print("\nArithmetic operations")
print(a+b) # Addition Operation (for string: Join strings)
print(a-b) # Subtraction Operation
print(a*b) # Multiplication Operation (for string: Repeat string)
print(a/b) # Division Operation gives integer result
print(a//b) # Floor Division Operation gives float result
print(a%b) # Modulus Operation gives reminder
print(a**b) # Exponentiation Operation gives power of number


# Assignment operators
print("\nAssignment operators")
a = 10 # Assigning a new value to a 
a += 5 # Increment a by 2 and then assign the result back to a
print(a) # print updated value of a
b -= 5.33 # Decrement by 5.33
print(b) # print updated value of b
c *= 3 # Repeat string c thrice
print(c) # Print updated value of c
a /= 2 # Divide a by 2 and assign the result back to a
print(a) # Print updated value of a

a =+ 3 # Means: assign positive 3 to a
print(a) # output: 3


# Comparison operators gives result in Boolean (TRUE/FALSE)
print("\nComparison operators")
print(a == b) # Check if a is equal to b
print(a != b) # Check if a is not equal to b
print(a > b) # Check if a is greater than b
print(a < b) # Check if a is less than b
print(a >= b) # Check if a is greater than or equal to b
print(a <= b) # Check if a is less than or equal to b


# Logical operations gives result in Boolean (TRUE/FALSE)
print("\nLogical operations")
print(a > 0 and b > 0) # Check if both a and b are greater than 0
print(a > 0 or b < 0) # Check if either a is greater than 0 or b is less than 0
print(not (a > b)) # Check if a is not greater than 0 (then o/p: True)
                   # Check if a is greater than 0 (then o/p: False)
print(a)

