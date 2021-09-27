"""
Author: chiu cam minh
Date: 04/08/2021
Program: project_01_page_132.py
Problem:
    Write a script that inputs a line of plaintext and a distance value and
    outputs an encrypted text using a Caesar cipher.
    The script should work for any printable characters.
Solution:
    
"""

def encrypt(plaintext):
    code = ""
    for ch in plaintext:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > 127:
            cipherValue = distance - (127 - ordValue + 1)
        code += chr(cipherValue)
    return code
    
    
plaintext = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
print(encrypt(plaintext))
