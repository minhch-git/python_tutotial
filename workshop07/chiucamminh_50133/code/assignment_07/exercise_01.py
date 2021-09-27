"""
Author: chiu cam minh
Date: 11/09/2021
Program: assignment_07_exercise_01.py
Problem:
   Define a function drawCircle. This function should expect a Turtle object,
   the coordinates of the circle’s center point, and the circle’s radius as arguments.
   The function should draw the specified circle.
   The algorithm should draw the circle’s circumference by turning 3 degrees and moving a given distance 120 times.
   Calculate the distance moved with the formula 2.0 * p * radius / 120.0.
Solution:
   
"""


from turtle import Turtle
from math import pi


def drawCircle(t, x, y, radius):
    degrees = 3
    distance = 2.0 * pi * radius / 120

    t.shape("turtle")
    t.color("purple")
    t.width(2)
    t.up()
    t.goto(x, y)
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.down()

    for count in range(120):
        t.forward(distance)
        t.left(degrees)


def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    radius = int(input("Enter radius: "))
    t = Turtle()
    drawCircle(t, x, y, radius)


if __name__ == "__main__":
    main()
