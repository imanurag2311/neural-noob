"""
Purpose: To print a random funny joke
Author: Anurag Yadav
Created: 27-07-2025
Language: Python (3.11.9)
Library: pyjokes
Status: Final
"""
# Install pyjokes library
# pip install pyjokes

import pyjokes

print("Printing joke...")
joke = pyjokes.get_joke()
print(joke)