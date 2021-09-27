"""
Author: chiu cam minh
Date: 13/07/2021
Program: project_10_page63.py

Problem:
  An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.
Solution:
  1. The inputs:
    the hourly wage
    total regular hours
    total overtime hours 
  2. Computations:
    totalWeeklyPay = the hourly wage * (total regular hours + total overtime hours)
  3. The outputs are:
    Displays an employee’s total weekly pay
"""

# Request the inputs
hourlyWage = float(input('Enter the hourly wage: '))
totalRegularHours = float(input('Enter total regular hours: '))
totalOvertimeHours  = float(input('Enter total overtime hours : '))

# Compute an employee’s total weekly pay
totalWeeklyPay = hourlyWage * (totalRegularHours + totalOvertimeHours)

# Display an employee’s total weekly pay
print(f'An employee’s total weekly pay is {totalWeeklyPay}')
