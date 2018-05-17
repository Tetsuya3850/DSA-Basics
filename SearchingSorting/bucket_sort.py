import math


def bucket_sort(A):
    # Time O(N), Space O(N), where N is the length of the array.
    buckets = [[] for _ in range(10)]
    for num in A:
        idx = math.floor(num * 10)
        buckets[idx].append(num)
    result = []
    for bucket in buckets:
        bucket.sort(reverse=True)
        while bucket:
            item = bucket.pop()
            result.append(item)
    return result


A = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(bucket_sort(A))
