"""
Author: chiu cam minh
Date: 02/09/2021
Program: exersice_04_page_182.py
Problem:
  Explain what happens when the following recursive function is called with the value 4 as an argument:
  def example(n):
    if n > 0:
      print(n)
      example(n - 1)
Solution:
  n = 4
    print(4)
    example(4 - 1)
      n = 3
        print(3)
        example(3 - 1)
          n = 2
            print(2)
            example(2 - 1)
              n = 1
              print(1)
                example(1 - 1)
                  n = 0
"""


def example(n):
    if n > 0:
        print(n)
        example(n - 1)


example(4)
