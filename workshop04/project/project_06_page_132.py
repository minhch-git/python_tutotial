"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_06_page_132.py
Problem:
    Use the strategy of the decimal to binary conversion and
    the bit shift left operation defined in Project 5 to code a new encryption algorithm.
    The algorithm should add 1 to each character’s numeric ASCII value, convert it to a bit string, 
    and shift the bits of this string one place to the left. A single-space character in 
    the encrypted string separates the resulting bit strings.
Solution:
    
"""
# conver decimal to binary
def convert_decimal_to_binary(decimal): 
    stack = []
    while decimal != 0:
        stack.append(decimal%2)
        decimal = decimal // 2
    result = ""
    while stack != [] :
        result += str(stack.pop())
    return result

plain_text = input("Enter a message: ")
code = ""

for ch in plain_text:
    # Add 1 to ASCII value
    ordValue = ord(ch) + 1
    # get binary string
    bString = convert_decimal_to_binary(ordValue)
    # Shift one bit to left
    if len(bString) > 1:
        bString = bString[1: ] + bString[0]
    # Add encrypted character to code string 
    code += bString + " "

print(code)
