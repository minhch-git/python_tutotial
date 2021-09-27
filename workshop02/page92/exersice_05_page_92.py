"""
Author: chiu cam minh
Date: 22/07/2021
Program: exersice_05_page92.py
Problem:
  What is the maximum number of guesses necessary to guess correctly a given number between the numbers N and M?

Solution:
  x = 55
  x = x + 1 or x += 1
"""

import random
min = int(input('Enter the smaller number: '))
max = int(input('Enter the larger number: '))
num = random.randint(min, max)
count = 0

while True: 
  count+=1
  inputNumber = int(input('Enter your guess: '))
  if inputNumber < num:
    print('Too small!')
  elif inputNumber > num:
    print('Too large!')
  else: 
    print("Congratulations! You've got it in", count,"tries!")
    break
