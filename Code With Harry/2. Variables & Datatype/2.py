"""
Purpose: Finding the type of variable and manually changing one type to another by typecasting
Author: Anurag Yadav
Created: 27-07-2025
Language: Python (3.11.9)
Status: Final
"""

a = 2
t = type(a) # <class 'int'>
print(t) # Print the type of variable a 

b = 21.663
t = type(b) # <class 'float'>
print(t) # Print the type of variable b

c = "Anurag Yadav"
t = type(c) # <class 'str'>
print(t) # Print the type of variable c

d = True
t = type(d) # <class 'bool'>
print(t) # Print the type of variable d

a = float(a) # Converting int to float by typecasting (manually changing one type to another)
t = type(a) # <class 'float'>
print(t) # Print the type of variable of a

b = int(b) # Converting float to int by typecasting
t = type(b) # <class 'int'>
print(t) # Print the type of variable of b

e = "10" 
t = type(e) # <class 'str'>
print(t) # Must give sting as type of variable

e = int(e) # converting string to int by typecasting
t = type(e) # <class 'int'>
print(t) # must give int as type of variable
