
def longest_contained_range(A):
    # Write a program which takes as input a set of integers represented by an array, and returns the size of a largest subset of integers in the array having the property that if two integers are in the subset, thenso are all integers betwen them.
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
