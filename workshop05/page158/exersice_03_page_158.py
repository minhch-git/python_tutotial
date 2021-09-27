"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_03_page_149.py
Problem:
  Assume that the variable data refers to the dictionary {'b':20, 'a':35}. 
  Write the expressions that perform the following tasks:
Solution:
  a. Replace the value at the key 'b' in data with that value’s negation.
  b. Add the key/value pair 'c':40 to data.
  c. Remove the value at key 'b' in data, safely.
  d. Print the keys in data in alphabetical order.
"""
data = {'b':20, 'a':35}
# a. Replace the value at the key 'b' in data with that value’s negation.
data['b'] = -data['b']
print(f"a. {data}")

# b. Add the key/value pair 'c':40 to data.
data['c'] = 40
print(f"b. {data}")

# c. Remove the value at key 'b' in data, safely.
theKeys = list(data.keys())
for key in theKeys:
  if key == 'b':
    data.pop('b')

print(f"c. {data}")

# d. Print the keys in data in alphabetical order.
keys = list(data.keys())
keys.sort()
print('d.')
for key in keys:
  print(data[key])
