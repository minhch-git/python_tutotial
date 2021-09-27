"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_07_page63.py

Problem:
  Write a program that calculates and prints the number of minutes in a year.
Solution:
  Calculates and prints the number of minutes in a year
  1. Significant constants
    DAY_IN_A_YEAR
    HOUR_IN_A_DAY
    MINUTES_IN_A_HOUR
  2. Computations:
    result = DAY_IN_A_YEAR * HOUR_IN_A_DAY * MINUTES_IN_A_HOUR
  3. The outputs are:
    The number of minutes in a year.

  # Initialize the constants
  DAY_IN_A_YEAR = 365
  HOUR_IN_A_DAY = 24
  MINUTES_IN_A_HOUR = 60

  # Compute the number of minutes in a year
  result = DAY_IN_A_YEAR * HOUR_IN_A_DAY * MINUTES_IN_A_HOUR
  result2 = result + HOUR_IN_A_DAY * MINUTES_IN_A_HOUR

  # Display the number of minutes in a year
  print(f'The number of minutes in a year(365 days) {result}')
  print(f'The number of minutes in a year(366 days) {result2}')

"""
# Initialize the constants
DAY_IN_A_YEAR = 365
HOUR_IN_A_DAY = 24
MINUTES_IN_A_HOUR = 60

# Compute the number of minutes in a year
result = DAY_IN_A_YEAR * HOUR_IN_A_DAY * MINUTES_IN_A_HOUR
result2 = result + HOUR_IN_A_DAY * MINUTES_IN_A_HOUR

# Display the number of minutes in a year
print(f'The number of minutes in a year(365 days) {result}')
print(f'The number of minutes in a year(366 days) {result2}')
