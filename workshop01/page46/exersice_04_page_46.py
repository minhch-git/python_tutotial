"""
Author: chiu cam minh
Date: 10/07/2021
Program: exersice_04_page46.py
Problem:
  What happens when the print function prints a string literal with embedded newline characters?
  
Solution:
  Because the backslash is used for escape sequences, it must be escaped to appear as a literal character in a string. Thus,print('\n') will display an extra newline.
    Example: print('I don\'t like it.\nI don\'t like it.')
"""
print('I don\'t like it.\nI don\'t like it.')
