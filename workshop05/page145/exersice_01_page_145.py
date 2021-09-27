"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_01_page_145.py
Problem:
    Assume that the variable data refers to the list [5, 3, 7].
    Write the values of the following expressions:
    a. data[2]
    b. data[-1]
    c. len(data)
    d. data[0:2]
    e. 0 in data
    f. data + [2, 10, 5]
    g. tuple(data)
Solution:
    a. 7
    b. 7
    c. 3
    d. [5, 3]
    d. False
    f. [5, 3, 7, 2, 10, 5]
    g. (5, 3, 7)
    
"""

data = [5, 3, 7]
print(f"a. {data[2]}")
print(f"b. {data[-1]}")
print(f"c. {len(data)}")
print(f"d. {data[0:2]}")
print(f"d. {0 in data}")
print(f"f. {data + [2, 10, 5]}")
print(f"g. {tuple(data)}")
