"""
Author: chiu cam minh
Date: 04/08/2021
Program: exersice_04_page_125.py
Problem:
    Write a code segment that prints the names of all of the items in the current working directory.

Solution:
    # get path current folder
    path_current_folder = os.getcwd()

    # the names of all of the items in the current folder
    list_items = os.listdir(path_current_folder)

"""

import os 
# get path current folder
path_current_folder = os.getcwd()

# the names of all of the items in the current folder
items = os.listdir(path_current_folder)

print(items)
