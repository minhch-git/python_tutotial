"""
Author: chiu cam minh
Date: 05/09/2021
Program: project_04_page_203.py
Problem:
   Restructure Newton’s method (Case Study 3.6) by decomposing it into three cooperating functions.
   The newton function can use either the recursive strategy of Project 1 or the iterative strategy of Case Study 3.6.
   The task of testing for the limit is assigned to a function named limitReached, 
   whereas the task of computing a new approximation is assigned to a function named improveEstimate. 
   Each function expects the relevant arguments and returns an appropriate value.
Solution:
   
"""
import math


def limitReached(x, estimate):
    return abs(x - estimate ** 2) <= 0.000001


def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2


def newton(x, estimate=1.0):
    if limitReached(x, estimate):
        return estimate
    else:
        estimate = newton(x, improveEstimate(x, estimate))
    return estimate


if __name__ == "__main__":
    while True:
        x = input("Enter a positive number or enter/return key to quit: ")
        if x == "":
            break
        print("The program's estimate: ", newton(float(x)))
        print("Python's estimate: ", math.sqrt(float(x)))
