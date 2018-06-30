
from functools import cmp_to_key


def largestNumber(nums):
    # Time O(NlogN), where N is the length of the array nums.
    def compare(a, b):
        a = str(a)
        b = str(b)
        if a+b > b+a:
            return 1
        elif a+b == b+a:
            return 0
        else:
            return -1

    nums.sort(key=cmp_to_key(compare), reverse=True)
    return str(int("".join([str(num) for num in nums])))
