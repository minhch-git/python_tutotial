"""
Author: chiu cam minh
Date: 03/09/2021
Program: exersice_03_page_194.py
Problem:
    What is the lifetime of a variable? Give an example.
Solution:   
    The lifetime of a variable is the duration of program execution during which it uses memory storage.
    Module variables exist for the lifetime of the program that uses them. 
    Parameters and temporary variables exist for the lifetime of a particular function call.

    # Example:
        x = 5
        def f():
            x = 10      # Attempt to reset x
        f()             # Does the top-level x change?
        print(x)        # No, this displays 5)
"""
x = 5


def f():
    x = 10
    b = x


f()
print(x)
