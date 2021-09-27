"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_02_page_145.py
Problem:
    Assume that the variable data refers to the list [5, 3, 7]. 
    Write the expressions that perform the following tasks:
    a. Replace the value at position 0 in data with that value’s negation.
    b. Add the value 10 to the end of data.
    c. Insert the value 22 at position 2 in data.
    d. Remove the value at position 1 in data.
    e. Add the values in the list newData to the end of data.
    f. Locate the index of the value 7 in data, safely.
    g. Sort the values in data.
Solution:
    
"""

data = [5, 3, 7]
# a. Replace the value at position 0 in data with that value’s negation.
data[0] = -5
print(f"a. {data}")
# b. Add the value 10 to the end of data.

data.append(10)
print(f"b. {data}")

# c. Insert the value 22 at position 2 in data.
data.insert(2, 22)
print(f"c. {data}")

# d. Remove the value at position 1 in data.
data.pop(0)
print(f"d. {data}")

# e. Add the values in the list newData to the end of data.
newData = [1,2,3]
data.extend(newData)
print(f"e. {data}")

# f. Locate the index of the value 7 in data, safely.
if 7 in data:
    print(f"f. {data.index(7)}")
else:
    print(-1)

# g. Sort the values in data.
data.sort()
print(data)
