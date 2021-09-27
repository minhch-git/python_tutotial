"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_03_page_109.py
Problem:
    You are given a string that was encoded by a Caesar cipher with an unknown distance value.
    The text can contain any of the printable ASCII characters. Suggest an algorithm for cracking this code.
    
Solution:
    Decode based on its numeric value and plus (secret)/some other special string
    get code, secret, distance

    valueDecode = ""
    value_length = len(code)-len(secret)
    value = code[0:value_length]

    # check secret
    if code.endswith(secret) == False: 
        return "Code wrong"

    # decode 
    for ch in value:
        oddOrd = ord(ch) - distance
        if oddOrd < 0:
            oddOrd = 127 - (distance - (0 - ord(ch) - 1))
        valueDecode += chr(oddOrd)

    print(valueDecode)

"""
def encrypt(value, distance, secret=""):
    code = ""
    # encrypt value
    for ch in value:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > 127:
            cipherValue = distance - (127 - ordValue + 1)
        code += chr(cipherValue)


    # return encrypt value + secret
    return code + secret

def decrypt(code, distance, secret=""):
    valueDecode = ""
    value_length = len(code)-len(secret)
    value = code[0:value_length]

    # check secret
    if code.endswith(secret) == False: 
        # throw exception
        return "Code wrong"

    # decode
    for ch in value:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue < 0:
            cipherValue =127 - (distance - (1 - ordValue))
        valueDecode += chr(cipherValue)
    return valueDecode


value_test = "vscode"
secret = "hello"
code_value = encrypt(value_test, 7, secret)
decode_value = decrypt(code_value, 7, secret)

print("code : ", value_test)
print("decode : ", decode_value)
print("compare : ", decode_value == value_test)
