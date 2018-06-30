from collections import defaultdict


def longest_subarray_same_frequency(A):
    # Time O(N), Space O(N), where N is the length of the array.
    diff_ar = [None] * len(A)
    diff = 0
    for i in range(len(A)):
        if A[i] == 'A':
            diff += 1
        elif A[i] == 'B':
            diff -= 1
        diff_ar[i] = diff

    diff_map = defaultdict()
    diff_map[0] = -1
    max_subar = [-1, -1]
    for i in range(len(diff_ar)):
        if diff_ar[i] not in diff_map:
            diff_map[diff_ar[i]] = i
        else:
            match = diff_map[diff_ar[i]]
            dist = i - match
            longest = max_subar[1] - max_subar[0]
            if dist > longest:
                max_subar = [match, i]

    return A[max_subar[0]+1: max_subar[1]+1]


print(longest_subarray_same_frequency(
    ['A', 'B', 'A', 'A', 'A', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'B', 'B']))
