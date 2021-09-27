"""
Author: chiu cam minh
Date: 05/08/2021
Program: project_12_page_132.py
Problem:
    The Payroll Department keeps a list of employee information for each pay period in a text file.
    The format of each line of the file is the following:
    <last name> <hourly wage> <hours worked>
    Write a program that inputs a file_name from the user and
    prints to the terminal a report of the wages paid to the employees for the given period. 
    The report should be in tabular format with the appropriate header. 
    Each line should contain an employee’s name, the hours worked, and the wages paid for that period.
Solution:
    
"""
# Take the inputs
file_name = input("Enter the file name: ")

# Open the input file 
input_file = open(file_name, 'r')

# Read the data and print the report
print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))
for line in input_file:
    dataList = line.split()
    name = dataList[0]
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours * payRate
    print("%-15s%6s%15s" % (name, hours, totalPay))
