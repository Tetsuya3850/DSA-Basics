import math


def quadratic_formula(a, b, c):
    one_ans = (-b + math.sqrt(b ** 2 - 4*a*c)) / 2 * a
    sec_ans = (-b - math.sqrt(b ** 2 - 4*a*c)) / 2 * a
    return one_ans, sec_ans


print(quadratic_formula(1, -2, -3))
