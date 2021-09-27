"""
Author: chiu cam minh
Date: 02/08/2021
Program: exersice_02_page_106.py
Problem:
    Assume that the variable data refers to the string "myprogram.exe".
    Write the expressions that perform the following tasks:
    a. Extract the substring "gram" from data.
    b. Truncate the extension ".exe" from data.
    c. Extract the character at the middle position from data.

Solution:
    data = "myprogram.exe"
    a.
        print(f"a. {data[5:9]}")
    b.
        # data = data[:-4]
        # print(f"b. {data}")
        print(f"b. {data[:-4]}")
    c. 
        print(f"c. {data[len(data)//2:]}")

    
"""

data = "myprogram.exe"
# a. Extract the substring "gram" from data.
print(f"a. {data[5:9]}")

# b. Truncate the extension ".exe" from data.
# data = data[:-4]
# print(f"b. {data}")
print(f"b. {data[:-4]}")

# c. Extract the character at the middle position from data.
print(f"c. {data[len(data)//2:]}")
