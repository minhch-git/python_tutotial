"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_06_page63.py

Problem:
  The kinetic energy of a moving object is given by the formula KE 1 2/ mv**2 where m is the object’s mass and v is its velocity. Modify the program you created in Project 5 so that it prints the object’s kinetic energy as well as its momentum. 

Solution:
  Calculate the kinetic energy
  1. The inputs:
    mass
    velocity
  2. Computations:
    KE = 1 / 2 mv**2
  3. The outputs are:
    The kinetic energy

  # Request the inputs
  mass = float(input('Enter the mass(kg): '))
  velocity = float(input('Enter velocity(m/s): '))

  #  Compute the kinetic energyomentum
  kineticEnergyomentum = 1 / 2 * mass * velocity ** 2

  # Display the kinetic energyomentum
  print(f'The kinetic energyomentum is {kineticEnergyomentum}')
"""

# Request the inputs
mass = float(input('Enter the mass(kg): '))
velocity = float(input('Enter velocity(m/s): '))

# Compute the kinetic energyomentum
kineticEnergyomentum = 1 / 2 * mass * velocity ** 2

# Display the kinetic energyomentum
print(f'The kinetic energyomentum is {kineticEnergyomentum}')
