"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_02_page63.py
Problem:
  You can calculate the surface area of a cube if you know the length of an edge.Write a program that takes the length of an edge (an integer) as input and prints the cube’s surface area as output.
Solution:
  Calculate the surface area of a cube
  1. The inputs:
    edge
  2. Computations:
    area = 6 * edge**2
  3. The outputs are:
   The surface area of a cube

  # Request the inputs
  edge = float(input("Enter the cube's edge: "))

  #  Compute the surface area of ​​a cube
  area = 6 * edge ** 2

  # Display the surface area of ​​a cube
  print(f"The surface area of ​​a cube is {str(area)} square units")
"""
# Request the inputs
edge = float(input("Enter the cube's edge: "))

# Compute the surface area of ​​a cube
area = 6 * edge ** 2

# Display the surface area of ​​a cube
print(f"The surface area of ​​a cube is {str(area)} square units")
