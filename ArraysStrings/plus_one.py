
def plus_one(A):
    # Time O(N), Space O(1), where N is the length of the array.
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one([9, 9, 9]))
