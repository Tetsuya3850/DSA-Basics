import heapq


def sort_approximately_sorted_array(sequence, k):
    # Time O(NlogK), Space O(K), where N is the length of the sequence and k is the max distance from correctly sorted position.
    min_heap = []
    i = 0
    while i < k:
        heapq.heappush(min_heap, sequence[i])
        i += 1

    while i < len(sequence):
        smallest = heapq.heappushpop(min_heap, sequence[i])
        print(smallest)
        i += 1

    while min_heap:
        smallest = heapq.heappop(min_heap)
        print(smallest)
