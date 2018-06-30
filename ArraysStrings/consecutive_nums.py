
def consecutive_nums(A):
    # Time O(N), Space O(N), where N is the length of the array.
    unprocessed = set(A)
    max_interval_size = 0
    while unprocessed:
        a = unprocessed.pop()
        lower = a-1
        while lower in unprocessed:
            unprocessed.remove(lower)
            lower -= 1
        upper = a+1
        while upper in unprocessed:
            unprocessed.remove(upper)
            upper += 1
        max_interval_size = max(max_interval_size, upper - lower - 1)
    return max_interval_size
