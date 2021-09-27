"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_04_page_149.py
Problem:
  Define a function named summation. This function expects two numbers, 
  named low and high, as arguments. The function computes and 
  returns the sum of the numbers between low and high, inclusive.
Solution:
  
"""

def summation(low, high):
  result = []
  while low < high-1:
    result.append(low+1)
    low += 1
  return result

print(summation(4, 10))
