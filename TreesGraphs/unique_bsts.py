
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def num_trees(n):
    # Time O(N^2), Space O(N), where n is the given number.
    def helper(n, cache):
        if not n:
            return 1
        if n not in cache:
            result = 0
            for i in range(n):
                result += helper(i, cache) * helper(n-i-1, cache)
            cache[n] = result
        return cache[n]

    cache = defaultdict()
    return helper(n, cache)


def generate_trees(n):
    def helper(nums):
        if not nums:
            return [None]
        results = []
        for i in range(len(nums)):
            left_results = helper(nums[:i])
            right_results = helper(nums[i+1:])
            for left_result in left_results:
                for right_result in right_results:
                    root = TreeNode(nums[i])
                    root.left = left_result
                    root.right = right_result
                    results.append(root)
        return results

    if not n:
        return []
    nums = [i for i in range(1, n+1)]
    return helper(nums)
