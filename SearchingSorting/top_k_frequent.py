
from collections import Counter


def top_k_frequent(nums, k):
    bucket = [None] * (len(nums) + 1)
    frequency_table = Counter()
    for num in nums:
        frequency_table[num] += 1

    for key, value in frequency_table.items():
        if bucket[value] == None:
            bucket[value] = []
        bucket[value].append(key)

    result = []
    pos = len(bucket) - 1
    while pos >= 0 and len(result) < k:
        if bucket[pos] != None:
            result.extend(bucket[pos])
        pos -= 1
    return result
