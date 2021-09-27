
"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_02_page_118.py
Problem:
    Using the value of data from Exercise 1, write the values of the following expressions:
    a. data.endswith('i')
    b. " totally ".join(data.split())

Solution:
    a. False
    b. Python totally rules!
"""

data = "Python rules!"

result_a = data.endswith('i')
print("a. ", result_a)

result_b =" totally ".join(data.split())
print("b. ", result_b)
