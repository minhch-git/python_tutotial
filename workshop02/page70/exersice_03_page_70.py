"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_03_page70.py
Problem:
  Explain the role of the variable in the header of a for loop.
  
Solution:
  The header often declares an explicit loop counter or loop variable, which allows the body to know which iteration is being executed.
  Example: for count range(10)
  variable: i has an execution count of 10
"""
# Example:
for i in range(10):
  print(i + 2)
