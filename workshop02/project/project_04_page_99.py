"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_04_page99.py
Problem:
  A standard science experiment is to drop a ball and see how high it bounces. Once the “bounciness” of the ball has been determined, the ratio gives a bounciness index. For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index is 0.6, and the total distance traveled by the ball is 16 feet after one bounce. If the ball were to continue bouncing, the distance after two bounces would be 10ft + 6ft + 6ft + 3.6ft = 5 25.6ft. Note that the distance traveled for each successive bounce is the distance to the floor plus 0.6 of that distance as the ball comes back up. Write a program that lets the user enter the initial height from which the ball is dropped and the number of times the ball is allowed to continue bouncing. Output should be the total distance traveled by the ball.

Solution:
  # Accept the inputs
  the user enter the initial height
  the number of times the ball

  # Compute
  total = 0
  while number_of_times > 0:
    total += height 
    height = height * BOUNCINESS_INDEX
    total += height
    number_of_times -= 1

  # Display 
  the total distance traveled by the ball.
"""

# Initialize
BOUNCINESS_INDEX = 0.6

# Accept the inputs
height = int(input("Enter the height: "))
number_of_times = int(input("Enter the number of times: "))

# Compute
total = 0
while number_of_times > 0:
  total += height 
  height = height * BOUNCINESS_INDEX
  total += height
  number_of_times -= 1

# Display
print(total)
