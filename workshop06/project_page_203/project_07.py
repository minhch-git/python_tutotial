"""
Author: chiu cam minh
Date: 05/09/2021
Program: project_07_page_203.py
Problem:
   Write a recursive function that expects a pathname as an argument.
   The path name can be either the name of a file or the name of a directory. 
   If the pathname refers to a file, its name is displayed, followed by its contents.
   Otherwise, if the pathname refers to a directory, the function is applied to each name in the directory.
   Test this function in a new program.
Solution:
"""
import os


def show_file(file_name):
    f = open(file_name, "r")
    for line in f:
        print(line)


def check_path(path):
    return os.path.isdir(path)


def find(path, x):
    space = ""
    for i in range(x):
        space += " "
        if check_path(path):
            for contents in os.listdir(path):
                content = os.path.join(path, contents)
                print(space + content)
                if check_path(content):
                    find(content, x + 1)
                else:
                    show_file(content)


def main():
    find(f"{os.getcwd()}/project_page_203", 2)


if __name__ == "__main__":
    main()
