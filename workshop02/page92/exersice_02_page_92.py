"""
Author: chiu cam minh
Date: 22/07/2021
Program: exersice_02_page_92.py
Problem:
  The factorial of an integer N is the product of the integers between 1 and N, inclusive. Write a while loop that computes the factorial of a given integer N.
  
Solution:
"""

# The input
number = int(input('Enter the number: '))

# check number > 0
if number > 0: 
  # init variable
  factorial = 1
  count = 1

  # compute
  while count <= number:
    factorial *= count
    count += 1

  # the output
  print(factorial)

# print error
print('Invalid input ')
