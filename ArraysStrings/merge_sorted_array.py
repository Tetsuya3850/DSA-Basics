# Merges two sorted arrays of integers.

def merge_sorted_array(A, B):
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

print (merge_sorted_array([1, 2, 7, 9], [7, 8, 9, 10]))
