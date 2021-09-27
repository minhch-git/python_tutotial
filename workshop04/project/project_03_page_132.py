"""
Author: chiu cam minh
Date: 04/08/2021
Program: project_03_page_132.py
Problem:
    Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.
Solution:
    
"""


# encryption
def encrypt(plaintext):
    code = ""
    for ch in plaintext:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
        if cipherValue > 127:
            cipherValue = distance - (127 - ordValue + 1)
        code += chr(cipherValue)
    return code
    
# decryption
def decrypt(code):
    plaintext = ""
    for ch in code:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue < 0:
            cipherValue =127 - (distance - (1 - ordValue))
        plaintext += chr(cipherValue)
    return plaintext
    

while True: 
    print("1. Encrypt content file")
    print("2. Decrypt content file")
    print("3. Exit!")
    choose = int(input("-- choose -- "))
    if choose == 1:
        # Take the inputs
        in_file_name = input("Enter the input file name: ")
        out_file_name = input("Enter the out file name: ")
        distance = int(input("Enter the distance value: "))

        # Open the input file and read plain text
        input_file = open(in_file_name, 'r')
        plain_text = input_file.read()
        print(f"plain text: {plain_text}")

        # Open the output file name and write the encrypted text
        out_file = open(out_file_name, 'w')
        code = encrypt(plain_text)

        print(f"code : {code}")

        out_file.write(code)
        out_file.close()

    elif choose == 2:
        # Take the inputs
        in_file_name = input("Enter the input file name: ")
        out_file_name = input("Enter the out file name: ")
        distance = int(input("Enter the distance value: "))

        # Open the input file and read plain text
        input_file = open(in_file_name, 'r')
        code = input_file.read()
        print(f"Code: {code}")

        # Open the output file name and write the encrypted text
        out_file = open(out_file_name, 'w')
        plain_text = decrypt(code)

        print(f"plain_text : {plain_text}")

        out_file.write(plain_text)
        out_file.close()
        
    elif choose == 3:
        print("Good bye!!!")
        break
