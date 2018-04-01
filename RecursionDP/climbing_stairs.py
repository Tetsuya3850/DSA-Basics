# Count how many ways to run up stairs. You can hop 1~3 steps.

def stair_ways(n):
    def stair_helper(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif cache[n]:
            return cache[n]
        else:
            cache[n] = stair_helper(n - 1) + stair_helper(n - 2) + stair_helper(n - 3)
            return cache[n]
    cache = [0] * (n + 1)
    return stair_helper(n)

print (stair_ways(5))


def stair_ways_iter(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n <= 2:
        return n
    else:
        a = 1
        b = 1
        c = 2
        for i in range(3, n+1):
            d = a + b + c
            a = b
            b = c
            c = d
        return c

print (stair_ways_iter(3))
