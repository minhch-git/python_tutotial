"""
Author: chiu cam minh
Date: 12/07/2021
Program: exersice_01_page59.py
Problem:
  Explain the relationship between a function and its arguments.


Solution:
  A function is a chunk of code that can be called by name to perform a task. Functions often require arguments, that is, specific data values, to perform their tasks.
  Some functions have only optional arguments, some have required arguments, and some have both required and optional arguments.

  Example: In function round(8.558, 2)
    8.558 is required argument, 
    2     is optional argument

"""
# TypeError: round() missing required argument 'number'
# print(round())

# true
print(round(8.558))
print(round(8.558, 2))
