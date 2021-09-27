"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_09_page_132.py
Problem:
    Write a script named numberlines.py. This script creates a program listing from a source program.
    This script should prompt the user for the names of two files. 
    The input filename could be the name of the script itself, but be careful to use a different output filename!
    The script copies the lines of text from the input file to the output file, numbering each line as it goes.
    The line numbers should be right-justified in 4 columns,
    so that the format of a line in the output file looks like this example:
    1> This is the first line of text.
Solution:
    
"""

# take the inputs 
in_file_name = input("Enter the input file name: ")
out_file_name = input("Enter the out file name: ")

# open the input file and write the text
out_file = open(out_file_name, 'w')

# open the output files 
with open(in_file_name, 'r') as file:
    i = 0
    for line in file:
        i += 1
        print(line)
        out_file.write(f'{i}> {line}')
        
out_file.close()
