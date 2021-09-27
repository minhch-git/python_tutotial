"""
Author: chiu cam minh
Date: 22/07/2021
Program: project_01_page99.py
Problem:
  Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is a right tri angle. Recall from the Pythagorean theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides.

Solution:
  Check equilateral triangle
  1. The input
    Three sides of a triangle
  2. Compute
    Pythagorean: true 
    if Pythagorean: 
      output='yes'
    else:
      output='no'
  3. ouput:
    print(output)
"""

# 1. The input
first_edge = int(input('Enter the first edge: '))
second_edge = int(input('Enter the second edge: '))
three_edge = int(input('Enter the three sides: '))

# 2. Compute
pythagorean = first_edge ** 2 == second_edge ** 2 + three_edge ** 2 or second_edge ** 2 == first_edge ** 2 + three_edge ** 2 or second_edge ** 2 + first_edge ** 2 == three_edge ** 2 

if pythagorean:
  output = 'Yes'
else:
  output = 'No'
# 3. ouput:
print(f'The triangle is a right triangle: {output}')
