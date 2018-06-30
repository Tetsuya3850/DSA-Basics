
import math


def kth_dictionary(nums, k):
    # Time O(N^2), Space O(1), where N is the length of the array.
    def shift_right(nums, s, e):
        # Time O(N), Spae O(1), where N is the length of the array.
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
        shift_right(nums, i, i+index)
        k %= factorial
    return nums


print(kth_dictionary([1, 2, 3, 4], 23))
print(kth_dictionary([1, 2, 3, 4], 45))
