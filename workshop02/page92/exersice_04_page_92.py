"""
Author: chiu cam minh
Date: 22/07/2021
Program: exersice_04_page92.py
Problem:
  Describe the purpose of the break statement and the type of problem for which it is well suited.

Solution:
  The break statement can be used to exit a while loop from its body. The break state ment is usually used when the loop must perform at least one iteration. The loop header’s condition in that case is the value True. The break statement is nested in an if statement that tests for a termination condition.
  (Break: dùng để thoát khỏi vòng lặp while, hoặc for.)
  
  Example: 
    while True:
      print('a. Next')
      print('b. Exit!')
      answer = input("Choose the answer: ")
      if(answer == 'b'):
        break;
      print('Welcome')

"""
while True:
  print('a. Next')
  print('b. Exit!')
  answer = input("Choose the answer: ")
  if(answer == 'b'):
    break;
  print('Welcome')
  print('-------')
