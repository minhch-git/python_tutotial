"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_07_page_165.py
Problem:
    Write a program that inputs a text file.
    The program should print the unique words in the file in alphabetical order.
Solution:
    
"""
import os

in_name = input('Enter the input file name: ')

input_file = open(f"{os.getcwd()}/file_test/{in_name}", 'r')
uniqueWords = []

for line in input_file:
  words = line.split()
  for w in words:
    if not w in uniqueWords:
      uniqueWords.append(w)
  
uniqueWords.sort()

for w in uniqueWords:
  print(w)
