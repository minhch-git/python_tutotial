"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_03_page_109.py
Problem:
    Translate each of the following numbers to binary numbers:
    a. 47(8)
    b. 127(8)
    c. 64(8)
Solution:
    a. convert_octal_to_binary(47)
    b. convert_octal_to_binary(127)
    c. convert_octal_to_binary(64)
"""

def convert_octal_to_binary(number): 
    # check number
    for ch in str(number):
        if int(ch) >= 8:
            return "None"
            
    stack = []
    while number != 0:
        stack.append(number%2)
        number = number // 2
    
    result = ""
    while stack != [] :
        result += str(stack.pop())
    
    return result

result_a = convert_octal_to_binary(47)
result_b = convert_octal_to_binary(127)
result_c = convert_octal_to_binary(64)

print("a. ",result_a)
print("b. ",result_b)
print("c. ",result_c)
