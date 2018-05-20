def minSubArrayLen(target, nums):
    # Given an array of n positive integers and a positive integer s,
    # find the minimal length of a contiguous subarray of which the sum ≥ s.
    # If there isn't one, return 0 instead.
    # Time O(N), Space O(1), where N is the length of the array.
    min_size = float('inf')
    l_point, r_point = 0, 0
    total = 0
    while r_point < len(nums):
        while r_point < len(nums) and total < target:
            total += nums[r_point]
            r_point += 1
        while total >= target:
            min_size = min(min_size, r_point - l_point)
            total -= nums[l_point]
            l_point += 1
    return min_size if min_size != float('inf') else 0


from collections import Counter


def all_distinct_subarray(paragraph):
    # Given an array A, find the shortest subarray A[i, j] such that each distinct value present in A is also present in the subarray.
    # Time O(N), Space O(1), where N is the length of the array.
    keywords = set(paragraph)
    keywords_count = Counter(keywords)
    result = [-1, -1]
    remaining_to_cover = len(keywords)
    left = 0
    right = 0
    while right < len(paragraph):
        while right < len(paragraph) and remaining_to_cover > 0:
            next_word = paragraph[right]
            if next_word in keywords:
                keywords_count[next_word] -= 1
                if keywords_count[next_word] >= 0:
                    remaining_to_cover -= 1
            right += 1

        while remaining_to_cover == 0:
            if result == [-1, -1] or (right - left) < (result[1] - result[0]):
                result = [left, right-1]
            left_word = paragraph[left]
            if left_word in keywords:
                keywords_count[left_word] += 1
                if keywords_count[left_word] > 0:
                    remaining_to_cover += 1
            left += 1

    return result


A = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat',
     'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
print(all_distinct_subarray(A))
