

import math


def kth_dictionary(nums, k):
    # Compute the kth permutation of array 1 to n under dictionary ordering.
    # Time O(N2), Space O(1), where N is the length of nums array.

    def shiftRight(nums, s, e):
        # Move element in pos e to pos s and shift other elements to right by 1.
        # Time O(N), Spae O(1), where N is the length of nums array.
        temp = nums[e]
        for i in reversed(range(s+1, e+1)):
            nums[i] = nums[i-1]
        nums[s] = temp

    n = len(nums)

    if k > math.factorial(n):
        return False

    k -= 1
    for i in range(n-1):
        factorial = math.factorial(n-i-1)
        index = k // factorial
        shiftRight(nums, i, i+index)
        k = k % factorial
    return nums


print(kth_dictionary([1, 2, 3, 4], 23))
print(kth_dictionary([1, 2, 3, 4], 45))
