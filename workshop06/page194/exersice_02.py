"""
Author: chiu cam minh
Date: 03/09/2021
Program: exersice_02_page_194.py
Problem:
    What is the scope of a variable? Give an example.
Solution:   
    The scope of a variable is the area of program text within which it has a given value. 
    The scope of a module variable is the text of the module below the variable’s introduction 
    and the bodies of any function definitions.
    The scope of a parameter is the body of its function definition.
    The scope of a temporary variable is the text of the function body below its introduction.

    # Example: 
        a = 12
        def sum():
            b = 8
            return a + b

        print(sum())
        #it will give an error because it is not the public variable on the function 
        # print(b)
"""

# Example:
a = 12


def sum():
    b = 8
    return a + b


print(sum())
# it will give an error because it is not the public variable on the function
# print(b)
