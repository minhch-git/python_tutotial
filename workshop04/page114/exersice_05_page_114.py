"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_05_page_109.py
Problem:
    Translate each of the following numbers to decimal numbers:
    a. 47(16)
    b. 127(16)
    c. AA(16)
Solution:
   a. convert_HEX_to_decimal(47)
   b. convert_HEX_to_decimal(127)
   c. convert_HEX_to_decimal("AA")


"""

def convert_HEX_to_decimal(number): 
    number = str(number)
    exponent = len(number) - 1
    result = 0

    for ch in number:
        if ch == "A":
            ch = "10"
        elif ch == "B":
            ch = "11"
        elif ch == "C":
            ch = "12"
        elif ch == "D":
            ch = "13"
        elif ch == "E":
            ch = "14"
        elif ch == "F":
            ch = "15"
        
        result += int(ch) * 16 ** exponent
        exponent -= 1

    return result

result_a = convert_HEX_to_decimal(47)
result_b = convert_HEX_to_decimal(127)
result_c = convert_HEX_to_decimal("AA")

print("a. ",result_a)
print("b. ",result_b)
print("c. ",result_c)
