
def add(a, b):
    # Write a function that adds two numbers. You should not use any arithmetic operators
    # Time O(A + B), Space O(1), where A and B is the figure of a and b in binary.
    running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        running_sum |= ak ^ bk ^ carryin
        carryin, k, temp_a, temp_b = (
            carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
    return running_sum | carryin


print(add(3, 9))


def multiply(x, y):
    running_sum = 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


print(multiply(3, 9))


def divide(x, y):
    result = 0
    power = 32
    y_power = y << power
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1

        result += 1 << power
        x -= y_power
    return result


print(divide(81, 9))


def power(x, y):
    result = 1.0
    power = y
    if y < 0:
        power, x = -power, 1.0/x
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1
    return result


print(power(2, 3))


def reverse(x):
    result = 0
    x_remain = abs(x)
    while x_remain:
        result = result * 10 + x_remain % 10
        x_remain //= 10
    return -result if x < 0 else result


print(reverse(-314))
