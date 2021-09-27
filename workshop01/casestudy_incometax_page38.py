"""
Author: chiu cam minh
Date: 12/07/2021
Program: case_study_page_38.py
Problem:
  The customer requests a program that computes a person’s income tax.
  
Solution:
  Compute a person’s income tax.
  1. Significant constants
    tax rate
    standard deduction
    deduction per dependent
  2. The inputs are
    gross income
    number of dependents
  3. Computations:
    taxable income = gross income - the standard
    deduction - a deduction for each dependent
    income tax = is a fixed percentage of the taxable income
  4. The outputs are
    the income tax


  # Initialize the constants
  TAX_RATE = 0.20 # 
  STANDARD_DEDUCTION = 10000.0
  DEPENDENT_DEDUCTION = 3000.0

  # Request the inputs
  grossIncome = float(input("Enter the gross income: "))
  numDependents = int(input("Enter the number of dependents: "))   

  # Compute the income tax
  totalDeduction = STANDARD_DEDUCTION + DEPENDENT_DEDUCTION * numDependents
  taxableIncome = grossIncome - totalDeduction
  incomeTax = taxableIncome * TAX_RATE

  # Display the income tax
  print(f"The income tax is ${str(incomeTax)}")


  # Display the income tax
  print("The income tax is $" + str(incomeTax))
"""

# Initialize the constants
TAX_RATE = 0.20 # 
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))   

# Compute the income tax
totalDeduction = STANDARD_DEDUCTION + DEPENDENT_DEDUCTION * numDependents
taxableIncome = grossIncome - totalDeduction
incomeTax = taxableIncome * TAX_RATE

# Display the income tax
print(f"The income tax is ${str(incomeTax)}")
