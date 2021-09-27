"""
Author: chiu cam minh
Date: 02/09/2021
Program: exersice_05_page_182.py
Problem:
  Explain what happens when the following recursive function is called with the value 4 as an argument:
  def example(n):
    if n > 0:
      print(n)
      example(n)
    else: 
      example(n - 1)
Solution:
    Infinite recursion arises.
    Could not identify the base case or to reduce the size of 
    the problem in such a way that the recursion ends.
    
    n = 4 is always greater than 0

"""


def example(n):
    if n > 0:
        print(n)
        example(n)
    else:
        example(n - 1)


example(4)
