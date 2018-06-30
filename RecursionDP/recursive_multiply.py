
def multiply_recursive(a, b):
    # Time O(logk), Space O(logk), where k is the smaller of the two.
    def multiply_helper(smaller, bigger):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return bigger
        half = smaller >> 1
        half_prod = multiply_helper(half, bigger)
        if a % 2 == 0:
            return half_prod + half_prod
        else:
            return half_prod + half_prod + bigger

    bigger = max(a, b)
    smaller = min(a, b)
    return multiply_helper(smaller, bigger)


print(multiply_recursive(8, 9))
