
def largest_contiguous_subsequence(A):
    # Time O(N), Space O(1), where N is the length of the array.
    max_sum = 0
    curr_sum = 0
    for num in A:
        curr_sum += num
        if max_sum < curr_sum:
            max_sum = curr_sum
        elif curr_sum < 0:
            curr_sum = 0
    return max_sum


print(largest_contiguous_subsequence([5, -9, 6, -2, 3]))
