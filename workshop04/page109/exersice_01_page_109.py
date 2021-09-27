"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_01_page_109.py
Problem:
    Write the encrypted text of each of the following words using a Caesar cipher with a distance value of 3:
        a. python
        b. hacker
        c. wow
Solution:
    encrypted_a = encrypt(text_a, distance)
    encrypted_b = encrypt(text_b, distance)
    encrypted_c = encrypt(text_c, distance)
    
"""

def encrypt(value, distance):
    code = ""
    for ch in value:
        ordvalue = ord(ch)
        cipherValue = ordvalue + distance

        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('z') - ordvalue + 1)

        code += chr(cipherValue)

    return code

text_a = "python"
text_b = "hacker"
text_c = "wow"

distance = 3
code = ""

encrypted_a = encrypt(text_a, distance)
encrypted_b = encrypt(text_b, distance)
encrypted_c = encrypt(text_c, distance)

print("a. ",encrypted_a)
print("b. ",encrypted_b)
print("c. ",encrypted_c)
