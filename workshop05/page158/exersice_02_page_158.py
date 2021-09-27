"""
Author: chiu cam minh
Date: 10/08/2021
Program: exersice_02_page_158.py
Problem:
  Assume that the variable data refers to the dictionary {'b':20, 'a':35}. 
  Write the values of the following expressions:
  a. data['a']
  b. data.get('c', None)
  c. len(data)
  d. data.keys()
  e. data.values()
  f. data.pop('b')
  g. data # After the pop above
Solution:
  a. 35
  b. None
  c. 2
  d. dict_keys(['b', 'a'])
  e. dict_values([20, 35])
  f. {'a': 35}
  g. {'a': 35}
"""

data =  {'b': 20, 'a': 35 }
print(f"a. {data['a']}")
print(f"b. {data.get('c', None)}")
print(f"c. {len(data)}")
print(f"d. {data.keys()}")
print(f"e. { data.values()}")
data.pop('b')
print(f"f. {data}")
print(f"g. {data}")
