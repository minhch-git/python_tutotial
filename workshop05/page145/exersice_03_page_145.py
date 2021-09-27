"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_03_page_145.py
Problem:
    What is a mutator method?
    Explain why mutator methods usually return the value None.
Solution:
    The functions and methods examined in previous chapters return a value that 
    the caller can then use to complete its work. 
    Mutable objects (such as lists) have some methods devoted entirely to modifying 
    the internal state of the object.
    Such methods are called mutators.

    Because a change of state is all that is desired,
    a mutator method usually returns no value of interest to the caller
    Python nevertheless automatically returns the special value None even
    when a method does not explicitly return a value.
"""
