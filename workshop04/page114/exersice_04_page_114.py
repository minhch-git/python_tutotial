"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_04_page_109.py
Problem:
    Translate each of the following numbers to decimal numbers:
    a. 47(8)
    b. 127(8)
    c. 64(8)
Solution:
    a. convert_octal_to_decimal(47)
    b. convert_octal_to_decimal(127)
    c. convert_octal_to_decimal(64)

"""

def convert_octal_to_decimal(number): 
    number = str(number)
    exponent = len(number) - 1
    result = 0

    for ch in number:
        # check number
        if int(ch) >= 8:
            return "None"
        result += int(ch) * 8 ** exponent
        exponent -= 1

    return result

result_a = convert_octal_to_decimal(47)
result_b = convert_octal_to_decimal(127)
result_c = convert_octal_to_decimal(64)

print("a. ",result_a)
print("b. ",result_b)
print("c. ",result_c)
