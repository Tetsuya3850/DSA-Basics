
import sys
import math


def binary_search_division(x, y):
    left, right = 0, sys.float_info.max
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        if y * mid > x:
            right = mid
        else:
            left = mid
    return left


x = 4.0
y = 0.1
print(binary_search_division(x, y))
