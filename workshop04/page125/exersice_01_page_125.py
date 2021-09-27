"""
Author: chiu cam minh
Date: 04/08/2021
Program: exersice_01_page_125.py
Problem:
    Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file
Solution:
    # write random: 
    for count in range(500):
        number = random.randint(1, 500)
        file_write.write(str(number) + '\n')
    file_write.close()

    # prints the number of lines
    theSum = 0
    for line in file_read:
        theSum += number
"""


import random, os
file_write = open(f'{os.getcwd()}/page125/myfile.text', 'w')

print("Current working directery: ", os.getcwd())


for count in range(500):
    number = random.randint(994, 1023)
    file_write.write(str(number) + '\n')
file_write.close()

file_read = open(f'{os.getcwd()}/page125/myfile.text', 'r')
theSum = 0
for line in file_read:
    theSum += number
file_read.close()

print("The sum is", theSum)
