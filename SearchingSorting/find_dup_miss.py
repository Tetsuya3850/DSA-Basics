
def find_dup_miss(A):
    miss_XOR_dup = 0
    for i, num in enumerate(A):
        miss_XOR_dup ^= i
        miss_XOR_dup ^= num
    differ_bit = miss_XOR_dup & (~(miss_XOR_dup - 1))
    miss_or_dup = 0
    for i, num in enumerate(A):
        if i & differ_bit:
            miss_or_dup ^= i
        if num & differ_bit:
            miss_or_dup ^= num
    if any(num == miss_or_dup for num in A):
        return (miss_or_dup, miss_or_dup ^ miss_XOR_dup)
    else:
        return (miss_or_dup ^ miss_XOR_dup, miss_or_dup)


print(find_dup_miss([5, 3, 0, 1, 2, 3]))
