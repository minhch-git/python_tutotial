"""
Author: chiu cam minh
Date: 04/08/2021
Program: project_02_page_132.py
Problem:
    Write a script that inputs a line of encrypted text and a distance value and 
    outputs plaintext using a Caesar cipher.
    The script should work for any printable characters.
Solution:
    
"""

def decrypt(code):
    plaintext = ""
    for ch in code:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue < 0:
            cipherValue =127 - (distance - (1 - ordValue))
        plaintext += chr(cipherValue)
    return plaintext
    
    
coded = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
print(decrypt(coded))
