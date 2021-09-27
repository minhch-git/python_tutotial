"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_02_page_109.py
Problem:
    Translate each of the following numbers to decimal numbers:
    a. 11001(2)
    b. 100000(2)
    c. 11111(2)

Solution:
    Result: 
    a.  25
    b.  32
    c.  31
"""
def convert_binary_to_decimal(value): 
    exponent = len(value) - 1
    result = 0
    for ch in value:
        result += int(ch) * 2 ** exponent
        exponent = exponent - 1
    return result

result_a = convert_binary_to_decimal("11001")
result_b = convert_binary_to_decimal("100000")
result_c = convert_binary_to_decimal("11111")

print("a. ",result_a)
print("b. ",result_b)
print("c. ",result_c)
