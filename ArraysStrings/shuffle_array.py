
import random
from collections import defaultdict


def shuffle_array(A):
    # Time O(N). Space O(1), where N is the length of the array.
    for i in range(len(A)):
        k = random.randint(i, len(A) - 1)
        A[i], A[k] = A[k], A[i]
    return A


dic = defaultdict(int)
for _ in range(7200):
    dic[tuple(shuffle_array([1, 2, 3, 4]))] += 1
print(dic)


def random_set(A, m):
    # Time complexity O(m). Space complexity O(1), where m is the length of randome set.
    for i in range(m):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[:m]


dic2 = defaultdict(int)
for _ in range(720000):
    dic2[tuple(random_set([1, 2, 3, 4], 2))] += 1
print(dic2)


def continuous_random(it, k):
    sampling_results = [1] * k
    num_seen_so_far = k
    for x in it:
        num_seen_so_far += 1
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results
