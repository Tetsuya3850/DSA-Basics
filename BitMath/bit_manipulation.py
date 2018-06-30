
import math


def get_bit(n, i):
    return n & (1 << i)


def set_bit(n, i):
    return n | (1 << i)


def clear_bit(n, i):
    return n & ~(1 << i)


def toggle_bit(n, i):
    return n ^ (1 << i)


def update_bit(n, i, bit):
    n = clear_bit(n, i)
    return n | (bit << i)


def clear_left(n, i):
    # Clear bits from the most siginificant bit to i.
    return n & ((1 << i) - 1)


def clear_right(n, i):
    # Clear bits from i to least significant bit.
    return n & (-1 << (i + 1))


def clear_i_j(n, i, j):
    # Clear the bits j through i in N.
    upper_mask = (-1 << j + 1)
    lower_mask = (1 << i) - 1
    mask = upper_mask | lower_mask
    return n & mask


def clear_leftmost_bit(n):
    return n & (n-1)


def set_right(n, p):
    # Insert p ones on the right
    return n | ((1 << p) - 1)


def flip_bits(x):
    return x ^ ~0


def reverseBits(n):
    result = 0
    digits = 32
    while digits:
        result <<= 1
        result |= (n & 1)
        n >>= 1
        digits -= 1
    return result


def swap_odd_even_bits(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x


def swap_values(a, b):
    convert = a ^ b
    a ^= convert
    b ^= convert
    return a, b


def multiply_twoK(n, k):
    return n << k


def divide_twoK(n, k):
    return n >> k


def get_digits(n):
    return math.floor(math.log2(n) + 1)
