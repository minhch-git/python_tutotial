"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_09_page99.py

Problem:
  Write a program that receives a series of numbers from the user and allows the user to press the enter key to indicate that he or she is finished providing inputs. After the user presses the enter key, the program should print the sum of the numbers and their average.

Solution:


"""
theSum = 0.0
average = 0.0
value = input("Enter a number or press Enter to quit: ")
count = 0
while True:
  if value == '':
    count += count == 0 and 1
    break

  number = float(value)
  theSum += number
  count += 1
  value = input("Enter a number or press Enter to quit: ")

average =  theSum/count
print("The sum of the numbers is: ", theSum)
print("The average of the numbers is: ", average)
