import random

def shuffle_array(A):
    n = len(A)
    for i in range(n-1):
        k = random.randrange(i, n - 1)
        A[i], A[k] = A[k], A[i]
    return A

print (shuffle_array([1, 2, 3, 4]))
