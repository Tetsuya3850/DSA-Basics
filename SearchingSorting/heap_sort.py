import heapq


def heap_sort(A):
    # Time O(NlogN), Space O(1), where N is the length of the array.
    heapq.heapify(A)
    result = []
    while A:
        result.append(heapq.heappop(A))
    return result


A = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(A))
