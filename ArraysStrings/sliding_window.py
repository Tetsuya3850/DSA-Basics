def minSubArrayLen(target, nums):
    # Given an array of n positive integers and a positive integer s,
    # find the minimal length of a contiguous subarray of which the sum ≥ s.
    # If there isn't one, return 0 instead.
    # Time O(N), Space O(1), where N is the length of the array.
    min_size = float('inf')
    l_point, r_point = 0, 0
    total = 0
    while r_point < len(nums):
        while r_point < len(nums) and total < target:
            total += nums[r_point]
            r_point += 1
        while total >= target:
            min_size = min(min_size, r_point - l_point)
            total -= nums[l_point]
            l_point += 1
    return min_size if min_size != float('inf') else 0
