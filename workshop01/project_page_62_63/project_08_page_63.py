"""
Author: chiu cam minh
Date: 13/07/2021
Program: project_08_page63.py
Problem:
  Light travels at 3 *10**8 meters per second. A light-year is the distance a light beam travels in one year. Write a program that calculates and displays the value of a light-year.
Solution:
  Calculates the value of a light-year
  1. Significant constants
    DAY_IN_A_YEAR
    HOUR_IN_A_DAY
    MINUTES_IN_A_HOUR
    SECONDS_IN_A_MINUTES
  2. Computations:
    seconds in a year = DAY_IN_A_YEAR*HOUR_IN_A_DAY *MINUTES_IN_A_HOUR* SECONDS_IN_A_MINUTES
    #rate = 3*10**8 meters per second
    lightYear = Seconds in a year * rate
  3. The outputs are:
    The value of a light-year
"""
# Initialize the constants
DAY_IN_A_YEAR = 365
HOUR_IN_A_DAY = 24
MINUTES_IN_A_HOUR = 60
SECONDS_IN_A_MINUTES = 60

# Compute the value of a light-year
rate = 3*10**8
secondsInAYear = DAY_IN_A_YEAR * HOUR_IN_A_DAY * MINUTES_IN_A_HOUR * SECONDS_IN_A_MINUTES
lightYear = rate * secondsInAYear

# Display the value of a light-year
print(f'The value of a light-year {lightYear} meters')
