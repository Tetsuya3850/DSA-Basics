
from bisect import bisect_left


def intersect_sorted_array(A, B):
    # Time O(A+B), Space O(1), where A is the length of the array A and B is the length of the array B.
    i = 0
    j = 0
    result = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                result.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return result


print(intersect_sorted_array([2, 4, 5, 8], [3, 4, 7, 8]))


def intersect_sorted_array_binary_search(A, B):
    # Time O(AlogB), Space O(1), where A is the length of the array A and B is the length of the array B.
    def binary_search(A, x):
        i = bisect_left(A, x)
        return i != len(A) and A[i] == x

    result = []
    for num in A:
        if binary_search(B, num):
            result.append(num)
    return result


print(intersect_sorted_array_binary_search([2, 4, 5, 8], [3, 4, 7, 8]))
