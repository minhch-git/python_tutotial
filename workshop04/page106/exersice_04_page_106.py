"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_04_page_106.py
Problem:
    Assume that the variable myString refers to a string, and 
    the variable reversedString refers to an empty string. 
    Write a loop that adds the characters from myString to reversedString in reverse order.
Solution:
    
    
"""

my_string = "Write a loop that adds the characters from myString to reversedString in reverse order."
reversed_string = ''
index = len(my_string)-1

while index >= 0:
    reversed_string += my_string[index]
    index -= 1

print(reversed_string)
