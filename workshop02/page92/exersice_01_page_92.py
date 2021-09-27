"""
Author: chiu cam minh
Date: 22/07/2021
Program: exersice_01_page_92.py
Problem:
  Translate the following for loops to equivalent while loops:
  a. for count in range(100):
        print(count)
  b. for count in range(1, 101):
        print(count)
  c. for count in range(100, 0, –1):
        print(count)
  
Solution:
  a.count_a = 0
    while count_a < 100:
      print(count_a)
      count_a += 1
  
  b.count_b = 1
    while count_b < 101:
      print(count_b)
      count_b += 1


  c.count_c = 100
    while count_c > 0:
      print(count_c)
      count_c -= 1
  

"""
# a.
count_a = 0
while count_a < 100:
  print(count_a)
  count_a += 1

# b.
count_b = 1
while count_b < 101:
  print(count_b)
  count_b += 1

# c.
count_c = 100
while count_c > 0:
  print(count_c)
  count_c -= 1
