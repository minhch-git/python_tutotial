"""
Author: chiu cam minh
Date: 11/09/2021
"""


# Câu 1 (2.0 điểm). Viết hàm in các số nguyên tố trong khoảng từ 30 đến 200
import math


def cau01():
    for number in range(30, 100, 1):
        if number % 2 == 0:
            continue
        count = 0
        for i in range(2, int(math.sqrt(number)) + 1, 1):
            if number % i == 0:
                count = count + 1
        if count == 0:
            print(number)


if __name__ == "__main__":
    cau01()
