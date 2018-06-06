from collections import Counter


def all_distinct_subarray(paragraph):
    # Given an array A, find the shortest subarray A[i, j] such that each distinct value present in A is also present in the subarray.
    # Time O(N), Space O(k), where N is the length of the array and k is the num of distinct keywords.
    keywords = set(paragraph)
    keywords_count = Counter(keywords)
    result = (-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    right = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_count[p] -= 1
            if keywords_count[p] == 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == (-1, -1) or (right - left) < (result[1] - result[0]):
                result = (left, right)
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


def longest_subarray_with_distinct_entries(A):
    # Time O(N), Space O(k), where N is the length of the array and k is the num of distinct keywords.
    most_recent_occur = {}
    longest_dup_free_start_idx = 0
    result = 0
    for i, num in enumerate(A):
        if num in most_recent_occur:
            dup_idx = most_recent_occur[num]

            if dup_idx >= longest_dup_free_start_idx:
                result = max(result, i - longest_dup_free_start_idx)
                longest_dup_free_start_idx = dup_idx + 1
        most_recent_occur[num] = i
    return max(result, len(A) - longest_dup_free_start_idx)
