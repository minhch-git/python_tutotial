"""
Author: chiu cam minh
Date: 04/08/2021
Program: exersice_05_page_125.py
Problem:
    Write a code segment that prompts the user for a filename.
    If the file exists, the program should print its contents on the terminal.
    Otherwise, it should print an error message
    
Solution:
    path_current_folder = f"{os.getcwd()}/page125"
    def check_file_name(filename):
        # get all current folder
        items = os.listdir(path_current_folder)
        for item in items:
            return os.path.isfile(f'{path_current_folder}/{filename}')
                

    search_file_name = input("Enter a file name: ")
    if check_file_name(search_file_name):
        print(open(f"{path_current_folder}/{search_file_name}", 'r').read())
    else: print("File is not exist!")
    
"""
import os 
path_current_folder = f"{os.getcwd()}/page125"
def check_file_name(filename):
    # get all current folder
    items = os.listdir(path_current_folder)
    for item in items:
        return os.path.isfile(f'{path_current_folder}/{filename}')
            

search_file_name = input("Enter a file name: ")
if check_file_name(search_file_name):
    print(open(f"{path_current_folder}/{search_file_name}", 'r').read())
else: print("File is not exist!")
