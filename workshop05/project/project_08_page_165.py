"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_08_page_165.py
Problem:
    A file concordance tracks the unique words in a file and their frequencies.
    Write a program that displays a concordance for a file.
    The program should output the unique words and their frequencies in alphabetical order.
    Variations are to track sequences of two words and their frequencies, 
    or n words and their frequencies.
Solution:
    
"""
import os

in_name = input('Enter the input file name: ')

input_file = open(f"{os.getcwd()}/file_test/{in_name}", 'r')
uniqueWords = {}

for line in input_file:
  words = line.split()
  
  for w in words:
    freq = uniqueWords.get(w, None)
    if freq == None:
      uniqueWords[w] = 1
    else:
      uniqueWords[w] = freq + 1

words = list(uniqueWords.keys())
words.sort()

for w in uniqueWords:
  print(w, uniqueWords[w])
