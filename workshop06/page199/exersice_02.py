"""
Author: chiu cam minh
Date: 04/09/2021
Program: exersice_02_page_199.py
Problem:
   Write the code for a filtering that generates a list of the positive numbers in a list named numbers. 
   You should use a lambda to create the auxiliary function.
Solution:
   numbers = [23, 5, 2, -2, -5]
   print(list(filter(lambda n: n > 0, numbers)))

"""

numbers = [23, 5, 2, -2, -5]
print(list(filter(lambda n: n > 0, numbers)))
