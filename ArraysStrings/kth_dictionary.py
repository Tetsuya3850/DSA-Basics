# Compute the kth permutation under dictionary ordering, starting from the identity permutation.

import math


def kth_dictionary(n, k):
    def shiftRight(nums, s, e):
        temp = nums[e]
        for i in reversed(range(s+1, e+1)):
            nums[i] = nums[i-1]
        nums[s] = temp

    nums = [str(i) for i in range(1, n+1)]

    if k > math.factorial(n):
        return False

    k -= 1
    for i in range(n-1):
        factorial = math.factorial(n-i-1)
        index = k // factorial
        shiftRight(nums, i, i+index)
        k = k % factorial
    return nums


print(kth_dictionary(4, 23))
print(kth_dictionary(4, 45))
