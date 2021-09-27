"""
Author: chiu cam minh
Date: 05/09/2021
Program: project_10_page_203.py
Problem:
   Define and test a function myRange. 
   This function should behave like Python’s standard range function, with the required and optional arguments, 
   but it should return a list.
   Do not use the range function in your implementation! 
   (Hints: Study Python’s help on range to determine the names, positions, 
   and what to do with your function’s parameters.
   Use a default value of None for the two optional parameters.
   If these parameters both equal None, then the function has been called with just the stop value.
   If just the third parameter equals None,
   then the function has been called with a start value as well.
   Thus, the first part of the function’s code establishes what the values of the parameters are or should be.
   The rest of the code uses those values to build a list by counting up or down.)
Solution:
"""


def myRange(p1=None, p2=None, p3=None):
    args = []
    for i in [p1, p2, p3]:
        if i is not None:
            args.append(i)

    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start, stop, step = *args, 1
    elif len(args) == 3:
        start, stop, step = args
    res = []
    if step > 0:
        while start < stop:
            res.append(start)
            start += step
    else:
        while start > stop:
            res.append(start)
            start += step
    return res


def check_equal(actual, expected):
    print(f"my_range: {expected}, python_range: {actual}, Equal: {actual == expected}")


def main():
    check_equal(myRange(0), [])
    check_equal(myRange(20), list(range(20)))
    check_equal(myRange(0, 100, 3), list(range(0, 5, 2)))
    check_equal(myRange(6, 0, -2), list(range(6, 0, -2)))


if __name__ == "__main__":
    main()
