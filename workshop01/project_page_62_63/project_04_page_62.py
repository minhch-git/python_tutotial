"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_04_page63.py
Problem:
  Write a program that takes the radius of a sphere (a floating-point number) as input and then outputs the sphere’s diameter, circumference, surface area, and volume. 

Solution:
  Calculate the sphere’s diameter, circumference, surface area, and volume
  1. Significant constants
    PI
  2. The inputs:
    The radius of a sphere
  3. Computations:
    diameter      = 2 * radius
    circumference = diameter * PI
    area          = 4 * PI * radius * radius
    volume        = 4/3 * PI * radius * radius * radius
  4. The outputs are:
    The sphere’s diameter, circumference, surface area, and volume. 

  from math import pi
  # Initialize the constants
  PI = pi

  # Request the inputs
  radius = float(input('Enter the sphere’s radius: '))

  #  Compute the sphere’s diameter, circumference, surface area, and volume
  diameter      = 2 * radius
  circumference = diameter * PI
  area          = 4 * PI * radius * radius
  volume        = 4/3 * PI * radius * radius * radius

  # Display the sphere’s diameter, circumference, surface area, and volume
  print('Output of the sphere: ')
  print(f'Diameter: {diameter}')
  print(f'Circumference: {circumference}')
  print(f'Area: {area}')
  print(f'Volume: {volume}')

"""
from math import pi
# Initialize the constants
PI = pi

# Request the inputs
radius = float(input('Enter the sphere’s radius: '))

# Compute the sphere’s diameter, circumference, surface area, and volume
diameter      = 2 * radius
circumference = diameter * PI
area          = 4 * PI * radius * radius
volume        = 4/3 * PI * radius * radius * radius

# Display the sphere’s diameter, circumference, surface area, and volume
print('Output of the sphere: ')
print(f'Diameter: {diameter}')
print(f'Circumference: {circumference}')
print(f'Area: {area}')
print(f'Volume: {volume}')
