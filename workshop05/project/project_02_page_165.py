"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_02_page_165.py
Problem:
    Write a program that allows the user to navigate the lines of text in a file. 
    The program should prompt the user for a filename and input the lines of text into a list.
    The program then enters a loop in which it prints the number of lines 
    in the file and prompts the user for a line number.
    Actual line numbers range from 1 to the number of lines in the file. 
    If the input is 0, the program quits. 
    Otherwise, the program prints the line associated with that number.
Solution:
    
"""
import os
in_name = input('Enter the input file name: ')

input_file = open(f"{os.getcwd()}/file_test/{in_name}", 'r')
lines = []
for line in input_file:
  lines.append(line)


while True: 
  print('The file has', len(lines), "lines")
  if len(lines) == 0:
    break
  else:
    line_number = int(input("Enter a line number (0 to quit): "))
  if line_number == 0:
    break
  elif line_number >= len(lines):
    print('Error: line number must be less than', len(lines))    
  else:
    print(line_number, ': ', lines[line_number])
