"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_02_page_109.py
Problem:
    Consult the Table of ASCII values in Chapter 2 and suggest how you would modify the encryption and 
    decryption scripts in this section to work with strings containing all of the printable characters.

Solution:
    Encryption: "We have 128 characters in ASCII. If the character of the incremented value is greater than 128, convert it to the first character"
        # init distance, value
        # resolve: 
        Get ch in value
            newOrd = ord(ch) + distance
            if newOrd > 128:
                newOrd = distance - (128 - ord(ch) + 1)
            code += chr(newOrd)
        print(code)

    Decryption: If the character of the decrement value is less than 0, move it towards the last character
        get distance, valueCoded
        for ch in valueCoded:
            oddOrd = ord(ch) - distance
            if oddOrd < 0:
                oddOrd = 128 - (distance + (ord(ch) + 1))

            valueDec += chr(oddOrd)

        print(valueDec)

"""

# Encryption
value = "123!w32"
distance = 7
code = ""
for ch in value:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)

print(code)

# Decryption
valueCoded = "89:(~:9"
plaintext = ""
for ch in valueCoded:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue =127 - (distance - (1 - ordValue))
    plaintext += chr(cipherValue)

print(plaintext)
