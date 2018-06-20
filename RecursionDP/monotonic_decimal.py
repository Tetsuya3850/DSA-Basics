def monotonic_decimal(k):
    def helper(result, k):
        if len(result) == k:
            nonlocal results
            results.append(int(''.join(str(x) for x in result)))
            return
        start = result[-1] + 1 if result else 1
        for i in range(start, 10):
            result.append(i)
            helper(result, k)
            result.pop()

    if k > 9:
        return []
    results = []
    helper([], k)
    return results


print(monotonic_decimal(3))
