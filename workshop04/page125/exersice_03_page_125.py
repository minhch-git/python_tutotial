"""
Author: chiu cam minh
Date: 04/08/2021
Program: exersice_03_page_125.py
Problem:
    Assume that a file contains integers separated by newlines.
    Write a code segment that opens the file and prints the average value of the integers.

Solution:
    total = 0
    count = 0
    for line in file_read:
        wordlist = line.split()
        count += 1
        total += int(round(float(wordlist[0])))

    return total/count
"""

import os
file_read = open(f'{os.getcwd()}/page125/myfile.text', 'r')

total = 0
count = 0
for line in file_read:
    wordlist = line.split()
    total += int(round(float(wordlist[0])))
    count += 1

print("The number of four-letter words in the file is ", total/count)
