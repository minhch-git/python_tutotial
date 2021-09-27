"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_02_page_149.py
Problem:
  Define a function named even. This function expects a number as an argument and 
  returns True if the number is divisible by 2, or it returns False otherwise.
  (Hint: A number is evenly divisible by 2 if the remainder is 0.)
Solution:
  
"""

def even(number):
  if(number % 2 == 0):
    return True
  return False

print(even(4))
print(even(3))
print(even(0))
