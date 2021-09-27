"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_07_page_132.py
Problem:
    Write a script that decrypts a message coded by the method used in Project 6.
Solution:
    
"""

# conver binary to decimal
def convert_binary_to_decimal(binary): 
    exponent = len(binary) - 1
    decimal = 0
    for ch in binary:
        decimal += int(ch) * 2 ** exponent
        exponent = exponent - 1
    return decimal


code = input("Enter a message: ")
plain_text = ""
# convert string to array
binary_list = code.split(' ')
for binary in binary_list:
    # Shift one bit to right
    if len(binary) > 1:
        binary = binary[-1] + binary[:-1]
    # get decimal string
    plain_text += chr(convert_binary_to_decimal(binary) - 1)

print(plain_text)
