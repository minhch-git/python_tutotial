"""
Author: chiu cam minh
Date: 02/09/2021
Program: exersice_07_page_182.py
Problem:
Explain what happens when the following recursive function is called with the values "hello" and 0 as arguments:
    def example(aString, index):
        if index == len(aString):
            return ""
        else:
            return aString[index] + example(aString, index + 1)
Solution:
    example(hello, 0)
    index = 0 len(hello) = 5
    example(hello, 1)
    return "h"

    index = 1 len(hello) = 5
    example(hello, 2)
    return "h" + "e"

    index = 2 len(hello) = 5
    example(hello, 3)
    return "h" + "e" + "l"

    index = 3 len(hello) = 5
    example(hello, 4)
    return "h" + "e" + "l" + "l"

    index = 4 len(hello) = 5
    example(hello, 5)
    return "h" + "e" + "l" + "l" +"0"

    index = 5 len(hello) = 5 (break: index = len)

    return "hello"
"""


def example(aString, index):
    if index == len(aString):
        return ""
    else:
        return aString[index] + example(aString, index + 1)


print(example("hello", 0))
