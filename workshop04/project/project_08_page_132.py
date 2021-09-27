"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_08_page_132.py
Problem:
    Write a script named copyfile.py. This script should prompt the user for the names of two text files.
    The contents of the first file should be input and written to the second file.
Solution:
    
"""

# take the inputs 
in_file_name = input("Enter the input file name: ")
out_file_name = input("Enter the out file name: ")

# open the input file and read the text
input_file = open(in_file_name, 'r')
text = input_file.read()

# open the output file and write the text
out_file = open(out_file_name, 'w')
out_file.write(text)
out_file.close()
