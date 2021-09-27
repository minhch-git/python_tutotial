"""
Author: chiu cam minh
Date: 23/07/2021
Program: project_10_page99.py

Problem:
  The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%. Monthly payments are 5% of the listed purchase price, minus the down payment. Write a program that takes the purchase price as input. The program should display a table, with appropriate headers, of a pay ment schedule for the lifetime of the loan. Each row of the table should contain the following items:
  • the month number (beginning with 1)
  • the current total balance owed
  • the interest owed for that month
  • the amount of principal owed for that month
  • the payment for that month
  • the balance remaining after payment
  The amount of interest for a month is equal to balance * rate / 12. The amount of principal for a month is equal to the monthly payment minus the interest owed.

Solution:
"""


# The input
price = float(input('Enter the puchase price: '))
print('Month\t Balance owed\t Interest owed\t Principal Payment\t Balance remaining')
down_payment = 0.1 * price
month =0
balance_owed = price - down_payment
balance_remaining = balance_owed - balance_owed * 0.1   
balance_owed = price - down_payment
balance_remaining = balance_owed - balance_owed * 0.1 
principal_payment = balance_owed * 0.05  

while True:
  month += 1
  interest_owed = balance_owed * 0.1 / 12
  
  balance_remaining = balance_owed - principal_payment 
  print(month, round(balance_owed, 1), round(interest_owed, 2), round(principal_payment, 2), round(balance_remaining, 2))
  
  balance_owed = balance_remaining
  if int(balance_remaining) == 0:
    break
