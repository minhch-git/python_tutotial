"""
Author: chiu cam minh
Date: 22/07/2021
Program: project_03_page99.py
Problem:
  Modify the guessing-game program of Section 3.5 so that the user thinks of a number that the computer must guess. The computer must make no more than the minimum number of guesses, and it must prevent the user from cheating by entering misleading hints. (Hint: Use the math.log function to compute the minimum number of guesses needed after the lower and upper bounds are entered.)

Solution:
  import random, math

  # The input
  min = int(input('Enter the smaller number: '))
  max = int(input('Enter the larger number: '))
  limit = math.ceil(math.log(max - min))

  # init
  num = random.randint(min, max)
  count = 0
  print('------------------')
  print('Number of guesses: ', limit)
  print('------------------')

  # compute and display resut
  while count < limit: 
    count+=1
    input_number = int(input('Enter your guess: '))
    if(count==limit):
      print('Lose!')
    elif input_number < num:
      print('Too small!')
    elif input_number > num:
      print('Too large!')
    else: 
      print("Congratulations! You've got it in", count,"tries!")
      break
"""

import random, math

# The input
min = int(input('Enter the smaller number: '))
max = int(input('Enter the larger number: '))
limit = math.ceil(math.log(max - min))

# init
num = random.randint(min, max)
count = 0
print('------------------')
print('Number of guesses: ', limit)
print('------------------')

# compute and display resut
while count < limit: 
  count+=1
  input_number = int(input('Enter your guess: '))
  if(count==limit):
    print('Lose!')
  elif input_number < num:
    print('Too small!')
  elif input_number > num:
    print('Too large!')
  else: 
    print("Congratulations! You've got it in", count,"tries!")
    break
