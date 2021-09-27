"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_01_page72.py
Problem:
  Assume that the variable teststring refers to a string. Write a loop that prints each character in this string, followed by its ASCII value

Solution:
  teststring = 'hello everybody!'
  for char in teststring: 
    print(f'{char}: {ord(char)}')
 
"""
teststring = 'hello everybody!'
for char in teststring: 
  print(f'{char}: {ord(char)}')
