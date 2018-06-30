
def next_permutation(A):
    # Time O(N), Space O(1), where N is the length of the array.
    inversion_point = len(A) - 1
    while inversion_point >= 1 and A[inversion_point] <= A[inversion_point - 1]:
        inversion_point -= 1
    if inversion_point == 0:
        A.reverse()
    else:
        for i in reversed(range(inversion_point, len(A))):
            if A[i] > A[inversion_point - 1]:
                A[inversion_point - 1], A[i] = A[i], A[inversion_point - 1]
                break
        A[inversion_point:] = reversed(A[inversion_point:])
    return A


print(next_permutation([6, 2, 1, 5, 0, 3, 4]))
