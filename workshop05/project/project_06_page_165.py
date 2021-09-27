"""
Author: chiu cam minh
Date: 13/08/2021
Program: project_06_page_165.py
Problem:
    Define a function decimalToRep that returns the representation of an integer in a given base.
    The two arguments should be the integer and the base. 
    The function should return a string.
    It should use a lookup table that associates integers with digits.
    Include a main function that tests the conversion function with numbers in several bases.
Solution:
    
"""
rep_table = {
  0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
  5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
  15: 'F'
}

def decimal_to_rep(decimal, base):
  if decimal == 0:
    return '0'
  
  rep = ''
  while decimal > 0:
    remainder = decimal % base
    decimal = decimal // base
    rep = rep_table[remainder] + rep
  return rep

def main():
  print(decimal_to_rep(10,10))
  print(decimal_to_rep(10,8))
  print(decimal_to_rep(10,2))
  print(decimal_to_rep(10,16))

main()
