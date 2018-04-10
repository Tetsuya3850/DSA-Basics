import random
from collections import defaultdict

def shuffle_array(A):
    for i in range(len(A)):
        k = random.randint(i, len(A) - 1)
        A[i], A[k] = A[k], A[i]
    return A

dic = defaultdict(int)
for _ in range(7200):
    dic[tuple(shuffle_array([1, 2, 3, 4]))] += 1
print (dic)


def random_set(A, m):
    subset = A[:m]
    for i in range(m, len(A)):
        k = random.randint(0, i)
        if k < m:
            subset[k] = A[i]
    return subset

dic2 = defaultdict(int)
for _ in range(720000):
    dic2[tuple(random_set([1, 2, 3, 4], 2))] += 1
print (dic2)
