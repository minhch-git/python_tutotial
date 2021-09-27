"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_03_page85.py
Problem:
  Write a loop that counts the number of space characters in a string. Recall that the space character is represented as ' '.
Solution:

  testString = 'Hello all of you !'
  count = 0
  for character in testString:
    if(character == ' '):
      count += 1

  print(count)

"""
testString = 'Hello all of you !'
count = 0
for character in testString:
  if(character == ' '):
    count += 1

print(count)
