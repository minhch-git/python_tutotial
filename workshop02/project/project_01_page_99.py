"""
Author: chiu cam minh
Date: 22/07/2021
Program: project_01_page99.py
Problem:
  Write a program that accepts the lengths of three sides of a triangle as inputs.The program output should indicate whether or not the triangle is an equilateral triangle.
  
Solution:
  Check equilateral triangle
  1. The input
    Three sides of a triangle
  2. Compute
    if three sides are equal
      output = 'Yes'
    else 
      output = 'No'
  3. ouput:
    print(output)
"""

# 1. The input
first_edge = int(input('Enter the first edge: '))
second_edge = int(input('Enter the second edge: '))
three_edge = int(input('Enter the three sides: '))
# 2. Compute
if first_edge == second_edge == three_edge:
  output = 'Yes'
else:
  output = 'No'
# 3. ouput:
print(f'The triangle is a equilateral triangle: {output}')
