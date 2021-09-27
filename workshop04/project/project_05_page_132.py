"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_05_page_132.py
Problem:
    A bit shift is a procedure whereby the bits in a bit string are moved to the left or to the right.
    For example, we can shift the bits in the string 1011 two places to the left to produce the string 1110.
    Note that the leftmost two bits are wrapped around to the right side of the string in this operation.
    Define two scripts, shiftLeft.py and shiftRight.py, that expect a bit string as an input.
    The script shiftLeft shifts the bits in its input one place to the left, 
    wrapping the leftmost bit to the rightmost position.
    The script shiftRight performs the inverse operation.
    Each script prints the resulting string.
Solution:
    
"""

while True: 
    print("1. Shift left")
    print("2. Shift right")
    print("3. Exit!")
    choose = int(input("-- choose -- "))
    if choose == 1:
        bitsL = input("Enter a string of bits: ")
        if len(bitsL) > 1:
            bitsL = bitsL[1: ] + bitsL[0]
        print(bitsL)

    elif choose == 2:
        bitsR = input("Enter a string of bits: ")
        if len(bitsR) > 1:
            bitsR = bitsR[-1] + bitsR[:-1]
        print(bitsR)

    elif choose == 3:
        print("Good bye!!!")
        break
