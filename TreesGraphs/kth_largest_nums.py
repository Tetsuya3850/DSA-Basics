
import heapq


def kth_largest_nums(nums, k):
    # Time O(Nlogk), Space O(1), where N is the length of nums and k is the length of result.
    result = []
    for num in nums:
        if len(result) < k:
            heapq.heappush(result, num)
        elif num > result[0]:
            heapq.heappop(result)
            heapq.heappush(result, num)
    return result


print(kth_largest_nums([3, 1, 5, 4, 2, 6], 4))
