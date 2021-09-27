"""
Author: chiu cam minh
Date: 02/09/2021
Program: exersice_06_page_182.py
Problem:
  Explain what happens when the following recursive function is called with the values "hello" and 0 as arguments:
  def example(aString, index):
    if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end = "")
Solution:
    example(hello,0)
    aString = hello, index = 0, len(hello) = 5
    aString[4] = o
    
    example(hello,1)
    aString = hello, index = 1, len(hello) = 5
    aString[3] = l
    
    example(hello,2)
    aString = hello, index = 2, len(hello) = 5
    aString[2] = l
  
    example(hello,3)
    aString = hello, index = 3, len(hello) = 5
    aString[1] = e
    
    example(hello,4)
    aString = hello, index = 4, len(hello) = 5
    aString[0] = h

    example(hello,5)
    aString = hello, index = 5, len(hello) = 5 ( break: index = len)

    olleh
"""


def example(aString, index):
    if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end="")


example("hello", 0)
