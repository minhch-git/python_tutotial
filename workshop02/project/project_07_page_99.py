"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_07_page63.py

Problem:
  Teachers in most school districts are paid on a schedule that provides a salary based on their number of years of teaching experience. For example, a beginning teacher in the Lexington School District might be paid $30,000 the first year. For each year of experience after this first year, up to 10 years, the teacher receives a 2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting salary, the percentage increase, and the number of years in the schedule. Each row in the schedule should contain the year number and the salary for that year.

Solution:
  1. The inputs:
    the starting salary, the percentage increase, and the number of years
  2. Compute
  3. output
    Displays a salary schedule, in tabular format
"""
# 1. The inputs:
start_salary = float(input("Enter the starting salary: "))
percen_increase = float(input("Enter the percentage increase: "))
number_of_years = int(input("Enter the number of years: "))

# initail variable
limit_year = 10
salary = 0.0
count = 1
percen_increase = percen_increase/100

# compute and display result
print("-----------------------------")
print(f"year number\t percentage\t salary")
while count <= number_of_years:
  if count == 1:
    salary += start_salary
    # print(f"{count}\t 0\t\t {salary}")
    print('%4d%20.2f%20.2f'%(count, percen_increase,salary))
    count += 1
  else:
    percen_increase += 0.02
    salary += salary * percen_increase
    print('%4d%20.2f%20.2f'%(count, percen_increase,salary))
    count += 1
