"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_06_page_145.py
Problem:
  Write a loop that replaces each number in a list named data with its absolute value.
Solution:
    
"""

list = [0,1,5,-3,6,-8]
for i in list:
    if i < 0:
      list[list.index(i)] = abs(i)

print(list)
