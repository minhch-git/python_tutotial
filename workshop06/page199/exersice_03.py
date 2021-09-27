"""
Author: chiu cam minh
Date: 04/09/2021
Program: exersice_03_page_199.py
Problem:
   Write the code for a reducing that creates a single string from a list of strings named words.
Solution:
   from functools import reduce

   words = ["Write", "the", "code", "for", "a", "reducing", "that", "creates", "a" ,"single","string"]
   print(reduce(lambda x, y: x + " " + y, words))
"""
from functools import reduce

words = [
    "Write",
    "the",
    "code",
    "for",
    "a",
    "reducing",
    "that",
    "creates",
    "a",
    "single",
    "string",
]
print(reduce(lambda x, y: x + " " + y, words))
