
from collections import defaultdict


def count_eval(s, result):
    def helper(s, result, cache):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1 if (bool(int(s)) == result) else 0

        if (s, result) not in cache:
            ways = 0
            for i in range(1, len(s), 2):
                c = s[i]
                left = s[:i]
                right = s[i+1:]
                leftTrue = helper(left, True, cache)
                leftFalse = helper(left, False, cache)
                rightTrue = helper(right, True, cache)
                rightFalse = helper(right, False, cache)
                total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

                totalTrue = 0
                if c == '^':
                    totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
                elif c == '&':
                    totalTrue = leftTrue * rightTrue
                elif c == '|':
                    totalTrue = leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue

                subWays = totalTrue if result else total - totalTrue
                ways += subWays
            cache[(s, result)] = ways

        return cache[(s, result)]

    cache = defaultdict()
    return helper(s, result, cache)


print(count_eval('1^0|0|1', False))
print(count_eval('0&0&0&1^1|0', True))
