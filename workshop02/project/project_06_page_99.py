"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_06_page99.py
Problem:
  The German mathematician Gottfried Leibniz developed the following method to approximate the value of π:
  π/4 = 1 - 1/3 + 1/5 - 1/7 +  . . .
  Write a program that allows the user to specify the number of iterations used inthis approximation and that displays the resulting value.

Solution:
  1. the input
  number = int(input('Enter the number of terations: '))
  2. init variable
  result = 0.0
  increment = 1
  3.  compute
  for i in range(number):
    if i == 0:
      result = 1.0
    elif(i%2 == 0):
      increment += 2
      result += 1/increment
    else:
      increment += 2
      result -= 1/increment
  pi = result * 4
  4. output
  print(pi)

"""

# the input
number = int(input('Enter the number of terations: '))
# init variable
result = 0.0
increase = 1

# compute
for i in range(number):
  if i == 0:
    result = 1.0
  elif(i%2 == 0):
    increase += 2
    result += 1/increase
  else:
    increase += 2
    result -= 1/increase

pi = result * 4
# output
print(pi)
