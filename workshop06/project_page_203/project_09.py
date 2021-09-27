"""
Author: chiu cam minh
Date: 05/09/2021
Program: project_09_page_203.py
Problem:
   Write a program that computes and prints the average of the numbers in a text file.
   You should make use of two higher-order functions to simplify the design.
Solution:
"""
import os
from functools import reduce


def get_number_list(file_name):
    f = open(file_name, "r")
    strList = f.read().split("\n")
    numberList = list(map(lambda x: int(x), strList))
    return numberList


def getAverage(numbers):
    return reduce(lambda x, y: x + y, numbers) / len(numbers)


def main():
    file_name = input("Input the file name: ")  # temp.txt
    numbers_file = get_number_list(f"{os.getcwd()}/project_page_203/temp/{file_name}")
    average = getAverage(numbers_file)
    print(average)


if __name__ == "__main__":
    main()
