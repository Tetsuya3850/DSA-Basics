import heapq


def continuous_median(sequence):
    # O(logN), where N is the num of elements, per cycle.
    min_heap = []
    max_heap = []
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) == len(max_heap):
            print(0.5 * (min_heap[0] + (-max_heap[0])))
        else:
            print(min_heap[0])
