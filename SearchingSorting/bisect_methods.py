from bisect import bisect_left, bisect_right

# Locate the leftmost value exactly equal to x
def index(A, x):
    i = bisect_left(A, x)
    if i != len(A) and A[i] == x:
        return i
    raise ValueError

# Find rightmost value less than x
def find_lt(A, x):
    i = bisect_left(A, x)
    if i:
        return A[i-1]
    raise ValueError

# Find rightmost value less than or equal to x
def find_le(A, x):
    i = bisect_right(A, x)
    if i:
        return A[i-1]
    raise ValueError

# Find leftmost value greater than x
def find_gt(A, x):
    i = bisect_right(A, x)
    if i != len(A):
        return A[i]
    raise ValueError

# Find leftmost item greater than or equal to x
def find_ge(A, x):
    i = bisect_left(A, x)
    if i != len(A):
        return A[i]
    raise ValueError
