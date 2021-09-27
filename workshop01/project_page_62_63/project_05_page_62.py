"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_05_page63.py
Problem:
  An object’s momentum is its mass multiplied by its velocity. Write a program that accepts an object’s mass (in kilograms) and velocity (in meters per second) as inputs and then outputs its momentum.
Solution:
  Calculate an object’s momentum
  1. The inputs:
    mass
    velocity
  2. Computations:
    momentum = mass multiplied velocity
  3. The outputs are:
    Its momentum

  # Request the inputs
  mass = float(input('Enter the mass: '))
  velocity = float(input('Enter velocity: '))

  #  Compute the momentum
  momentum = mass * velocity

  # Display the momentum
  print(f'Momentum = {momentum}')


"""

# Request the inputs
mass = float(input('Enter the mass(kg): '))
velocity = float(input('Enter velocity(m/s): '))

# Compute momentum
momentum = mass * velocity

# Display momentum
print(f'Momentum = {momentum}')
