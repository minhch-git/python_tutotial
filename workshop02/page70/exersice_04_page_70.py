"""
Author: chiu cam minh
Date: 18/07/2021
Program: exersice_04_page70.py
Problem:
  Write a loop that prints the first 128 ASCII values followed by the corresponding characters (see the section on characters in Chapter 2). Be aware that most of the ASCII values in the range “0.31” belong to special control characters with no stan-dard print representation, so you might see strange symbols in the output for these values.

Solution:
  for count in range(128):
    print(count, chr(count))
 
"""
for count in range(128):
  print(count, chr(count))
