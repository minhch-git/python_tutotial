"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_05_page_145.py
Problem:
  Assume that data refers to a list of numbers, and result refers to an empty list.
  Write a loop that adds the nonzero values in data to the result list,
  keeping them in their relative positions and excluding the zeros.
Solution:
    
"""

list = [0,1,5,2,0,3,6,8]
result = []
for i in list:
    if i != 0:
      result.append(i)

print(result)
