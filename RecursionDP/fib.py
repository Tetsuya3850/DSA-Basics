def fib(n):
    # Time O(N), Space O(N), where N is the given num.
    def helper(n):
        if n <= 1:
            return n
        if cache[n] == None:
            cache[n] = helper(n-1) + helper(n-2)
        return cache[n]
    cache = [None] * (n+1)
    return helper(n)


print(fib(10))


def fib_iter(n):
    # Time O(N), Space O(1), where N is the num of steps of the stair.
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


print(fib_iter(10))
