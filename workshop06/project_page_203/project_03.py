"""
Author: chiu cam minh
Date: 05/09/2021
Program: project_03_page_203.py
Problem:
   Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton. 
   (Hint: The estimate of the square root should be passed as a second argument to the function.)
Solution:
   
"""
import math


def newton(x, estimate=1.0):
    if abs(x - estimate ** 2) <= 0.000001:
        return estimate
    else:
        estimate = newton(x, (estimate + x / estimate) / 2)
    return estimate


if __name__ == "__main__":
    while True:
        x = input("Enter a positive number or enter/return key to quit: ")
        if x == "":
            break
        print("The program's estimate: ", newton(float(x)))
        print("Python's estimate: ", math.sqrt(float(x)))
