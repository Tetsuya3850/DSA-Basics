import random

def shuffle_array(A):
    for i in range(len(A)-1):
        k = random.randrange(i, len(A) - 1)
        A[i], A[k] = A[k], A[i]
    return A

print (shuffle_array([1, 2, 3, 4]))
