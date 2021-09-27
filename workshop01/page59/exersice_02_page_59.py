"""
Author: chiu cam minh
Date: 12/07/2021
Program: exersice_02_page59.py
Problem:
  The math module includes a pow function that raises a number to a given power.
  The first argument is the number, and the second argument is the exponent. Write a code segment that imports this function and calls it to print the values 8**2 and 5**4

Solution:
  from math import pow

  numberFirst = int(input('number first: '))
  numberSecond = int(input('number second: '))
  result = pow(numberFirst, numberSecond)

  print(f'pow({numberFirst, numberSecond}): {result}')

  print(f'pow(8,2): {pow(8,2)}')
  print(f'pow(5,4): {pow(5,4)}')

"""

from math import pow

numberFirst = int(input('number first: '))
numberSecond = int(input('number second: '))
result = pow(numberFirst, numberSecond)

print(f'pow({numberFirst, numberSecond}): {result}')

print(f'pow(8,2): {pow(8,2)}')
print(f'pow(5,4): {pow(5,4)}')
