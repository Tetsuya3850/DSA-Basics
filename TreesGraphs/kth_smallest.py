import heapq


def kth_smallest(nums, k):
    heapq.heapify(nums)
    for _ in range(k-1):
        heapq.heappop(nums)
    return nums[0]


print(kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
