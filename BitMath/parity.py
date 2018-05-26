
# 16 bits num parity lookup table
PRECOMPUTED_PARITY = []


def parity(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^ PRECOMPUTED_PARITY[x >> (2 * MASK_SIZE) & BIT_MASK] ^ PRECOMPUTED_PARITY[x >> MASK_SIZE & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])


def parity_alternative(x):
    # Time O(logN)
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1
