"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_03_page63.py
Problem:
  Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who like to buy LP record albums. The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video can use to calculate the total charge for a customer’s video rentals. The program should prompt the user for the number of each type of video and output the total cost.
Solution:
  Calculate the total charge for a customer’s video rentals
  1. Significant constants
    new video price
    old video price

  2. The inputs:
     the number of new videos
     the number of oldies videos

  3. Computations:
    totalCost = number new videos * new video price + number old videos * old video price
  4. The outputs are:
    the total cost

  # Initialize the constants
  NEW_VIDEO_PRICE = 3.00
  OLD_VIDEO_PRICE = 2.00

  # Request the inputs
  newVideos = int(input("Enter the number of new videos: "))
  oldVideos = int(input("Enter the number of old videos: "))

  #  Compute the total cost
  totalCost = newVideos * NEW_VIDEO_PRICE + oldVideos * OLD_VIDEO_PRICE

  # Display the total cost
  print(f"The total cost is ${totalCost}")

"""
# Initialize the constants
NEW_VIDEO_PRICE = 3.00
OLD_VIDEO_PRICE = 2.00

# Request the inputs
newVideos = int(input("Enter the number of new videos: "))
oldVideos = int(input("Enter the number of old videos: "))

# Compute the total cost
totalCost = newVideos * NEW_VIDEO_PRICE + oldVideos * OLD_VIDEO_PRICE

# Display the total cost
print(f"The total cost is ${totalCost}")
