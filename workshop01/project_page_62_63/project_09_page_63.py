"""
Author: chiu cam minh
Date: 13/07/2021
Program: project_09_page63.py

Problem:
  Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
    • A kilometer represents 1/10000 of the distance between the North Pole and
    the equator.
    • There are 90 degrees, containing 60 minutes of arc each, between the North
    Pole and the equator.
    • A nautical mile is 1 minute of an arc.

Solution:
    Calculate the number of nautical miles
  1. The inputs:
    a number of kilometers
  2. Computations:
  # There are 90 degrees, containing 60 minutes of arc each
    degreesPerMin = 90*60
    a kilometer represents = 1/10000

    oneKilometers = degreesPerMin / 10000
    nautical = oneKilometers * a number of kilometers
  3. The outputs are:
    The corresponding number of nautical miles

"""

# Request the inputs
numberKilometers = float(input('Enter a number of kilometers: '))

# Compute 
degreesPerMin = 90*60
oneKilometers = degreesPerMin / 10000

numberNauticalMiles = oneKilometers * numberKilometers

# Display 
print(f'{numberKilometers} kilometers = {numberNauticalMiles} nautical miles')
