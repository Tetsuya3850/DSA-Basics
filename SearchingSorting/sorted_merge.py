
def sorted_merge(A, B):
    A_i = len(A) - 1
    B_i = len(B) - 1
    for _ in range(len(B)):
        A.append(None)
    merged_i = len(A) - 1
    while B_i >= 0:
        if A_i >= 0 and A[A_i] > B[B_i]:
            A[merged_i] = A[A_i]
            A_i -= 1
        else:
            A[merged_i] = B[B_i]
            B_i -= 1
        merged_i -= 1
    return A

print (sorted_merge([1, 3, 5, 7], [2, 4, 9]))
