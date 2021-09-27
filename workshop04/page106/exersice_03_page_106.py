"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_03_page_106.py
Problem:
    Assume that the variable myString refers to a string.
    Write a code segment that uses a loop to print the characters of the string in reverse order.
Solution:
    index = len(myString)-1
    while index >= 0:
        print(myString[index])
        index -= 1
"""

myString = "Write a code segment that uses a loop to print the characters of the string in reverse order."
index = len(myString)-1

while index >= 0:
    print(myString[index])
    index -= 1
