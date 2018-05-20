from collections import defaultdict


def combination(self, n, k):
    def helper(n, k):
        if k == 1 or n == k:
            return [[(i)] for i in range(1, n+1)]
        if (n, k) not in cache:
            results = []
            without_n = helper(n-1, k)
            with_n = helper(n-1, k-1)
            for comb in with_n:
                results.append(comb + [n])
            results.extend(without_n)
            cache[(n, k)] = results
        return cache[(n, k)]
    cache = defaultdict()
    return helper(n, k)
