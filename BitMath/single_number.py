def single_number(nums):
    # Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
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
