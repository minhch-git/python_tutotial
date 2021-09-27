"""
Author: chiu cam minh
Date: 02/09/2021
Program: exersice_03_page_182.py
Problem:
    Describe the costs and benefits of defining and using a recursive function.
Solution:
    The costs: 
        It is usually slower due to the overhead of maintaining the stack.
        It usually uses more memory for the stack.
    The benefits:
        Recursion adds clarity and (sometimes) reduces the time needed to write and 
        debug code (but doesn't necessarily reduce space requirements or speed of execution).
        Reduces time complexity.
        Performs better in solving problems based on tree structures.
"""
num = int(input("Enter a number: "))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(num))
