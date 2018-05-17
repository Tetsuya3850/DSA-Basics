from bisect import bisect_left, bisect_right

# Time O(logN), where N is the length of the array.


def index_l(A, x):
    # Locate the leftmost value exactly equal to x
    i = bisect_left(A, x)
    if i != len(A) and A[i] == x:
        return i
    raise ValueError


def index_r(A, x):
    # Find rightmost value exactly equal to x
    i = bisect_right(A, x)
    if i and A[i-1] == x:
        return i-1
    raise ValueError


def find_lt(A, x):
    # Find rightmost value less than x
    i = bisect_left(A, x)
    if i:
        return A[i-1]
    raise ValueError


def find_le(A, x):
    # Find rightmost value less than or equal to x
    i = bisect_right(A, x)
    if i:
        return A[i-1]
    raise ValueError


def find_gt(A, x):
    # Find leftmost value greater than x
    i = bisect_right(A, x)
    if i != len(A):
        return A[i]
    raise ValueError


def find_ge(A, x):
    # Find leftmost item greater than or equal to x
    i = bisect_left(A, x)
    if i != len(A):
        return A[i]
    raise ValueError
