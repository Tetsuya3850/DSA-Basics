def merge_sorted_array(A, B):
    # Merges two sorted arrays of integers.
    # Time O(A+B), Space O(B), where A is the length of the array A and B is the length of the array B.

    m = len(A) - 1
    n = len(B) - 1
    A.extend([None] * (n+1))
    write_index = len(A) - 1

    while m >= 0 and n >= 0:
        if A[m] >= B[n]:
            A[write_index] = A[m]
            m -= 1
        else:
            A[write_index] = B[n]
            n -= 1
        write_index -= 1
    while n >= 0:
        A[write_index] = B[n]
        write_index -= 1
        n -= 1
    return A


print(merge_sorted_array([1, 2, 7, 9], [7, 8, 9, 10]))


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
