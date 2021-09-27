"""
Author: chiu cam minh
Date: 04/09/2021
Program: project_06_page_203.py
Problem:
    Lee has discovered what he thinks is a clever recursive strategy for printing 
    the elements in a sequence (string, tuple, or list). 
    He reasons that he can get at the first element in a sequence using the 0 index,
    and he can obtain a sequence of the rest of the elements by slicing from index 1.
    This strategy is realized in a function that expects just the sequence as an argument.
    If the sequence is not empty, the first element in the sequence is printed and
    then a recursive call is executed. On each recursive call,
    the sequence argument is sliced using the range 1:.
    Here is Lee’s function definition: 
    def printAll(seq): 
        if seq: 
            print(seq[0]) 
            printAll(seq[1:])
    Write a script that tests this function and add code to trace the argument on each call.
    Does this function work as expected? If so, explain how it actually works, and describe any hidden costs in running it.
Solution:
    Does this function work as expected? YES
    seq = [2, 3, 5, 7, 3, 8]

    printAll(seq)
        print(seq[0]) # 2
        printAll(seq[1:]) #  [3, 5, 7, 3, 8]

    printAll(seq)
        print(seq[0]) # 3
        printAll(seq[1:]) #  [5, 7, 3, 8]

    printAll(seq)
        print(seq[0]) # 5
        printAll(seq[1:]) #  [7, 3, 8]

    printAll(seq)
        print(seq[0]) # 7
        printAll(seq[1:]) #  [3, 8]

    printAll(seq)
        print(seq[0]) # 3
        printAll(seq[1:]) #  [8]

    printAll(seq)
        print(seq[0]) # 8
        printAll(seq[1:]) #  []

    printAll(seq)
        #seq = [] => break;
"""


def printAll(seq):
    if seq:
        print(seq[0])
        printAll(seq[1:])


# sep: (string, tuple, or list).
seq = [2, 3, 5, 7, 3, 8]
printAll(seq)
