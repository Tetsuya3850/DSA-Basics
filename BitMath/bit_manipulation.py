
import math


def get_bit(n, i):
    return n & (1 << i)


print(get_bit(9, 0))


def set_bit(n, i):
    return n | (1 << i)


print(set_bit(8, 0))


# Insert p ones on the right
def set_right(n, p):
    return n | ((1 << p) - 1)


print(set_right(128, 2))


# Clear bits from the most siginificant bit to i.
def clear_left(n, i):
    return n & ((1 << i) - 1)


print(clear_left(130, 7))


# Clear bits from the i to least significant bit.
def clear_right(n, i):
    return n & (-1 << (i + 1))


print(clear_right(130, 6))


def clear_bit(n, i):
    return n & ~(1 << i)


print(clear_bit(9, 0))


# Clear the bits j through i in N.
def clear_i_j(n, i, j):
    upper_mask = (-1 << j + 1)
    lower_mask = (1 << i) - 1
    mask = upper_mask | lower_mask
    return n & mask


print(clear_i_j(86, 1, 4))


def clear_leftmost_bit(n):
    return n & (n-1)


print(clear_leftmost_bit(64))


def toggle_bit(n, i):
    return n ^ (1 << i)


print(toggle_bit(4, 2))


def update_bit(n, i, bit):
    n = clear_bit(n, i)
    return n | (bit << i)


print(update_bit(128, 1, 1))


def swap_odd_even_bits(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


print(swap_odd_even_bits(10))


def flip_bits(x):
    return x ^ ~0


print(flip_bits(7))


def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


print(swap_bits(73, 1, 6))


def multiply_twoK(n, k):
    return n << k


print(multiply_twoK(4, 2))


def divide_twoK(n, k):
    return n >> k


print(divide_twoK(4, 2))


def swap_values(a, b):
    convert = a ^ b
    a ^= convert
    b ^= convert
    return a, b


print(swap_values(4, 9))


def get_digits(n):
    return math.floor(math.log2(n) + 1)


print(get_digits(7))
