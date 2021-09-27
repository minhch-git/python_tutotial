"""
Author: chiu cam minh
Date: 04/08/2021
Program: project_04_page_132.py
Problem:
    Octal numbers have a base of eight and the digits 0–7.
    Write the scripts octalToDecimal.py and decimalToOctal.py,
    which convert numbers between the octal and decimal representations of integers.
    These scripts use algorithms that are similar to those of the binaryToDecimal and
    decimalToBinary scripts devel oped in Section 4-3.
Solution:
    
"""
def decimal_to_octal(decimal): 
    stack = []
    while decimal != 0:
        stack.append(decimal%8)
        decimal = decimal // 8
    
    result = ""
    while stack != [] :
        result += str(stack.pop())
    
    return result


def octal_to_decimal(octal): 
    octal = str(octal)
    exponent = len(octal) - 1
    decimal = 0

    for ch in octal:
        # check octal
        if int(ch) >= 8:
            return "None"
        decimal += int(ch) * 8 ** exponent
        exponent -= 1

    return decimal



while True: 
    print("1. Convert decimal to octal")
    print("2. Convert octal to decimal")
    print("3. Exit!")
    choose = int(input("-- choose -- "))
    if choose == 1:
        decimal = int(input("Enter a decimal integer: "))
        print(f"The octal representation {decimal_to_octal(decimal)}")

    elif choose == 2:
        octal = int(input("Enter a octal integer: "))
        print(f"The decimal representation {octal_to_decimal(octal)}")
    elif choose == 3:
        print("Good bye!!!")
        break
