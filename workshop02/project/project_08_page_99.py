"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_08_page99.py
Problem:
  The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive integers. You can use this algorithm in the following manner:
  a. Compute the remainder of dividing the larger number by the smaller number. 
  b. Replace the larger number with the smaller number and the smaller number with the remainder. 
  c. Repeat this process until the smaller number is zero.
  The larger number at this point is the GCD of A and B. Write a program that lets the user enter two integers and then prints each step in the process of using the Euclidean algorithm to find their GCD.

Solution:
  # The inputs
  The user enter two integers
  # Compute and display result
  prints each step in the process of using the Euclidean algorithm to find their GCD
  
  # Compute
  count = 0
  while b != 0:
    gcd = b
    b = a % b
    a = gcd
    print(f"Step {count}: {gcd}")
"""
# The inputs
a = int(input('Please input the first integer:'))
b = int(input('Please input the second integer:'))

# Compute and display result
count = 0
while b != 0:
  gcd = b
  b = a % b
  a = gcd
  print(f"Step {count}: {gcd}")
  count += 1
