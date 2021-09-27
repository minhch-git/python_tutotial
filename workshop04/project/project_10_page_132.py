"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_10_page_132.py
Problem:
    Write a script named dif.py. 
    This script should prompt the user for the names of two text files and
     compare the contents of the two files to see if they are the same.
     If they are, the script should simply output "Yes".
     If they are not, the script should output "No",
     followed by the first lines of each file that differ from each other.
     The input loop should read and compare lines from each file.
     The loop should break as soon as a pair of different lines is found.
Solution:
    
"""

# takes the inpust:
file_first_name = input("Enter the input file first name: ")
file_second_name = input("Enter the input file second name: ")

# Open the input file
file_first = open(file_first_name, 'r')
file_second = open(file_second_name, 'r')

# Read each pair of lines and compare them
while True: 
    line_file_first = file_first.readline()
    line_file_second = file_second.readline()
    if line_file_first == "" and line_file_second == "":
        print("Yes")
        break
    elif line_file_first != line_file_second:
        print("Node")
        print(line_file_first)
        print(line_file_second)
        break
