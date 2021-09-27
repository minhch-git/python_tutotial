"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_02_page_109.py
Problem:
    Translate each of the following numbers to binary numbers:
    a. 47(10)
    b. 127(10)
    c. 64(10)
Solution:
    Result: 
    a.  101111
    b.  1111111
    c.  1000000
"""

def convert_decimal_to_binary(number): 
    stack = []
    while number != 0:
        stack.append(number%2)
        number = number // 2
    
    result = ""
    while stack != [] :
        result += str(stack.pop())
    
    return result

result_a = convert_decimal_to_binary(47)
result_b = convert_decimal_to_binary(127)
result_c = convert_decimal_to_binary(64)

print("a. ",result_a)
print("b. ",result_b)
print("c. ",result_c)
