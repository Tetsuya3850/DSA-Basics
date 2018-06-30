def find_two_nums_appear_once(nums):
    # Time O(N), Space O(1), where N is the length of the array.
    xor = 0
    a = 0
    b = 0
    for num in nums:
        xor ^= num
    mask = xor & ~(xor-1)
    for num in nums:
        if num & mask:
            a ^= num
        else:
            b ^= num
    return (a, b)
