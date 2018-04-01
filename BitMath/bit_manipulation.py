
# Insert p ones on the right
def set_right(n, p):
    return n | ((1 << p) - 1)

print (set_right(128, 2))

# Clear bits from the right of p.
def clear_right(n, p):
    return n & -((1 << p) - 1)

print (clear_right(130, 7))


def clear_leftmost_bit(n):
    return n & (n-1)

print (clear_leftmost_bit(64))

# Clear the bits j through i in N.
def clear_i_j(n, i, j):
    upper_mask = (-1 << j + 1)
    lower_mask = (1 << i) - 1
    mask = upper_mask | lower_mask
    return n & mask

print (clear_i_j(86, 1, 4))

def swap_odd_even_bits(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

print (swap_odd_even_bits(10))
