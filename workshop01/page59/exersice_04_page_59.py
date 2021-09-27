"""
Author: chiu cam minh
Date: 12/07/2021
Program: exersice_04_page59.py
Problem:
  Explain how to display help information on a particular function in a given module.

  
Solution:
  import module
  help(module.namefunction)
  Example:
    import math
    help(math.cos)
    help(math.ceil)
    print(math.pi)

  If you are going to use only a couple of a module’s resources frequently, you can avoid the use of the qualifier with each reference by importing the individual resources.
  Example: 
  from math import pi, sqrt
  print(pi, sprt(2))
"""
import math
print(help(math.cos))
print(help(math.ceil))
