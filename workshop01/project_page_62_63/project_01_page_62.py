"""
Author: chiu cam minh
Date: 12/07/2021
Program: project_01_page63.py
Problem:
  The tax calculator program of the case study outputs a floating-point number
  that might show more than two digits of precision. Use the round function to
  modify the program to display at most two digits of precision in the output
  number.
Solution:
  Compute a person’s income tax.
  1. Significant constants
    tax rate: float
    standard deduction: float
    deduction per dependent: float
  2. The inputs are
    gross income: float
    number of dependents: int
  3. Computations:
    taxable income = gross income - the standard
    deduction - a deduction for each dependent
    income tax = is a fixed percentage of the taxable income
    most two digits of precision in the income tax
  4. The outputs are: round(ouput, 2)
    the income tax
  
  # Initialize the constants
  TAX_RATE = 0.20
  STANDARD_DEDUCTION = 10000.00
  DEPENDENT_DEDUCTION = 3000.00

  # Request the inputs
  grossIncome = float(input("Enter the gross income: "))
  numDependents = int(input("Enter the number of dependents: "))   

  # Compute the income tax
  totalDeduction = STANDARD_DEDUCTION + DEPENDENT_DEDUCTION * numDependents
  taxableIncome = grossIncome - totalDeduction
  incomeTax = taxableIncome * TAX_RATE

  # Display the income tax
  result=round(incomeTax, 2)
  print(f"The income tax is ${str(result)}")
"""

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 3000.00

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))   

# Compute the income tax
totalDeduction = STANDARD_DEDUCTION + DEPENDENT_DEDUCTION * numDependents
taxableIncome = grossIncome - totalDeduction
incomeTax = taxableIncome * TAX_RATE

# Display the income tax
result=round(incomeTax, 2)
print(f"The income tax is ${str(result)}")
