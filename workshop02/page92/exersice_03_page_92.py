"""
Author: chiu cam minh
Date: 22/07/2021
Program: exersice_03_page_92.py
Problem:
  The log(2) of a given number N is given by M in the equation N = 2**M . Using integer arithmetic, the value of M is approximately equal to the number of times N can be evenly divided by 2 until it becomes 0. Write a loop that computes this approximation of the log(2) of a given number N. You can check your code by importing the math.log function and evaluating the expression round(math.log(N, 2)) (note that the math.log function returns point value)
  
Solution:

"""
import math
# The input
n = int(input('Enter number: '))
# Check number
if n > 0:
  print(f"Math.log({n},2): {math.log(n, 2)}")
  m = 0

  # Loop
  while n > 0:
      m+=1
      n//=2

  # output
  print(f"Result: {m}")
else:
  print('Incorrect input')
  