# Write methods to implement the multiply, subtract, and divede opereations for integers. Thre results of all of these are integers. Use only the add opereator.


def negate(a):
    neg = 0
    new_sign = 1 if a < 0 else -1
    while a:
        neg += new_sign
        a += new_sign
    return neg


def abs(a):
    if a < 0:
        return negate(a)
    else:
        return a


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        result = negate(result)
    return result


def divide(a, b):
    if b == 0:
        return False
    abs_a = abs(a)
    abs_b = abs(b)

    product = 0
    x = 0
    while product + abs_b <= abs_a:
        product += abs_b
        x += 1
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        return x
    else:
        return negate(x)


print(subtract(9, -2))
print(multiply(9, -2))
print(multiply(-9, -2))
print(divide(10, -2))
print(divide(-10, -2))
