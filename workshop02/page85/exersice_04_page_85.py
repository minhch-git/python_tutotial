"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_04_page85.py
Problem:
  Assume that the variables x and y refer to strings. Write a code segment that prints these strings in alphabetical order. You should assume that they are not equal.

Solution:
  x = 'hello'
  y = 'Abcxyz'

  if y.lower()[0] > x.lower()[0]: 
    print(x,y)
  else:
    print(y,x)
"""
x = 'hello'
y = 'Abcxyz'

if y.lower()[0] > x.lower()[0]: 
  print(x,y)
else:
  print(y,x)
