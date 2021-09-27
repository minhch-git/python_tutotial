"""
Author: chiu cam minh
Date: 04/08/2021
Program: exersice_02_page_125.py
Problem:
    Write a code segment that opens a file for input and prints the number of four-letter words in the file.
Solution:
    count = 0
    for line in file_read:
        wordlist = line.split()
        if len(wordlist[0]) == 4:
            count += 1
    return count
"""

import os
file_read = open(f'{os.getcwd()}/page125/myfile.text', 'r')

count = 0
for line in file_read:
    wordlist = line.split()
    if len(wordlist[0]) == 4:
        count += 1

print("The number of four-letter words in the file is ", count)
