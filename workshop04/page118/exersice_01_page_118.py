
"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_01_page_118.py
Problem:
    Assume that the variable data refers to the string "Python rules!".
    Use a string method from Table 4-2 to perform the following tasks:
    a. Obtain a list of the words in the string.
    b. Convert the string to uppercase.
    c. Locate the position of the string "rules".
    d. Replace the exclamation point with a question mark.

Solution:
    a.  data.split()
    b.  data.upper()
    c.  data.find('rules')
    d.  data.replace('!', '?')

"""

data = "Python rules!"

# a. Obtain a list of the words in the string.
list = data.split()
print("a. ",list)

# b. Convert the string to uppercase.
strUpper = data.upper()
print("b. ",strUpper)

# c. Locate the position of the string "rules".
position = data.find('rules')
print("c. ",position)

# d. Replace the exclamation point with a question mark.
replaceMark = data.replace('!', '?')
print("d. ", replaceMark)
