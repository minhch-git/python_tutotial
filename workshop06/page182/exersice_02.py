"""
Author: chiu cam minh
Date: 02/09/2021
Program: exersice_02_page_182.py
Problem:
    The factorial of a positive integer n, fact(n), is defined recursively as follows:
        fact( n ) = 1, when n = 1
        fact( n ) = n * fact (n - 1) , otherwise
    Define a recursive function fact that returns the factorial of a given positive
    integer.

Solution:
"""
num = int(input("Enter a number: "))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(num))
