
import math


def square_root(x):
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid * mid
        if mid_squared > x:
            right = mid
        else:
            left = mid
        return left
