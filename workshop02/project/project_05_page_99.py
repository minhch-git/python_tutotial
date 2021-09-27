"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_05_page99.py
Problem:
  A local biologist needs a program to predict population growth. The inputs would be the initial number of organisms, the rate of growth (a real number greater than 0), the number of hours it takes to achieve this rate, and a number of hours during which the population grows. For example, one might start with a population of 500 organisms, a growth rate of 2, and a growth period to achieve this rate of 6 hours. Assuming that none of the organisms die, this would imply that this population would double in size every 6 hours. Thus, after allowing 6 hours for growth, we would have 1000 organisms, and after 12 hours, we would have 2000 organisms. Write a program that takes these inputs and displays a pre diction of the total population.

Solution:
  # Accept the inputs
  the number of organisms
  the rate of growth (a real number greater than 0), 
  the number of hours it takes to achieve this rate,
  a number of hours during which the population grows

  # Compute
  total_population = number_of_organisms
  while number_of_hours <= total_hours:
    total_population *= rate_of_grow
    number_of_hours *= 2
    
  # Display 
  Displays a prediction of the total population.
"""

# Initialize
total_population = 0

# The inputs:
number_of_organisms = int(input("The number of organisms: "))
rate_of_grow = int(input("The rate of growth (a real number greater than 0): "))
number_of_hours = int(input("The number of hours it takes to achieve this rate: "))
total_hours = int(input("Enter the total hours of growth: "))

# Compute
total_population = number_of_organisms
while number_of_hours <= total_hours:
  total_population *= rate_of_grow
  number_of_hours *= 2

# Display
print("the total population: ",total_population)
