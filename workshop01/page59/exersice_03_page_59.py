"""
Author: chiu cam minh
Date: 12/07/2021
Program: exersice_03_page59.py
Problem:
  Explain how to display a directory of all of the functions in a given module.
Solution:
  import module
  help(module)
  * To get the docs on all the functions at once, interactively. Or you can use:
  dir(module)
"""
import math
print(dir(math))
print(help(math))
