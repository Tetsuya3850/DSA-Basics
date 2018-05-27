def manhattan_dist(nums):
    # Time O(NlogN), Space O(1)
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)
