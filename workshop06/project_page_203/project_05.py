"""
Author: chiu cam minh
Date: 05/09/2021
Program: project_05_page_203.py
Problem:
   A list is sorted in ascending order if it is empty or each item except 
   the last one is less than or equal to its successor.
   Define a predicate isSorted that expects a list as an argument and 
   returns True if the list is sorted, or returns False otherwise.
   (Hint: For a list of length 2 or greater, loop through the list and compare pairs of items,
   from left to right, and return False if the first item in a pair is greater.)
Solution:
   
"""


def isSorted(list):
    result = True
    for i in range(1, len(list)):
        if list[i] >= list[i - 1]:
            continue
        else:
            result = False
            break
    return result


if __name__ == "__main__":
    # list = [6, 3, 4, 50]
    list = [3, 4, 6, 50]
    if isSorted(list):
        print("List is sorted!")
    else:
        print("List is not sorted!")
