
# Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.


def get_next(n):
    c = n
    c0 = 0
    c1 = 0

    while (c & 1) == 0 and c:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1

    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n


print(get_next(6))


def get_prev(n):
    c = n
    c0 = 0
    c1 = 0

    while (c & 1) == 1 and c:
        c1 += 1
        c >>= 1
    while (c & 1) == 0:
        c0 += 1
        c >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1

    n &= ~0 << p + 1
    mask = (1 << c1 + 1) - 1
    n |= mask << (c0 - 1)
    return n


print(get_prev(9))


def closest_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i+1)) & 1:
            x ^= (1 << i) | (1 << (i+1))
            return x
    raise ValueError('All bits are 0 or 1')


print(closest_int_same_bit_count(8))
