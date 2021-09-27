"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_02_page85.py
Problem:
  Assume that x refers to a number. Write a code segment that prints the number’s absolute value without using Python’s abs function.

Solution:
# The number’s absolute value
  x = -10
  if(x >= 0):
    print(x)
  else:
    print(-x)

"""
# The number’s absolute value
x = -10
if(x < 0):
  x = -x

print(x)
