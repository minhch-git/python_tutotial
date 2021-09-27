"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_04_page72.py
Problem:
  Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted in a column that is right-justified, with a field width of 12 and a precision of 2.

Solution:
  salaries = [1212, 1313.13,1414.141414,1515.151515,6616161.161616161]
  for amount in salaries:
    print('$%12.2f' %amount)

"""
salaries = [1212, 1313.13,1414.141414,1515.151515,6616161.161616161]
for amount in salaries:
  print('$%12.2f' %amount)
