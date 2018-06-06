
from collections import defaultdict


def combination(n, k):
    def helper(n, k):
        if k == 0:
            return [[]]
        if k == 1:
            return [[i] for i in range(1, n+1)]
        elif k == n:
            return [[i for i in range(1, n+1)]]
        if (n, k) not in cache:
            results = []
            without_n = helper(n-1, k)
            with_n = helper(n-1, k-1)
            for comb in with_n:
                comb.append(n)
            cache[(n, k)] = with_n + without_n
        return cache[(n, k)]
    cache = defaultdict()
    return helper(n, k)


print(combination(5, 4))


def combination_num(n, k):
    # Time O(nk), Space O(nk).
    def helper(n, k):
        if k == 0 or k == n:
            return 1
        if (n, k) not in cache:
            without_n = helper(n-1, k)
            with_n = helper(n-1, k-1)
            cache[(n, k)] = without_n + with_n
        return cache[(n, k)]
    cache = defaultdict()
    return helper(n, k)


print(combination_num(5, 3))
