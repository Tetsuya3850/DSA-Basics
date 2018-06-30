
def array_key_delete(A, k):
    # Time O(N), Space O(1), where N is the length of the array.
    write_index = 0
    for i in range(len(A)):
        if A[i] != k:
            A[write_index] = A[i]
            write_index += 1
    return A[:write_index]


print(array_key_delete([3, 11, 2, 3, 3, 7, 13, 3], 3))


def remove_duplicates(nums):
    # Time O(N), Space O(1), where N is the length of the array.
    if not nums:
        return
    write_index = 1
    for i in range(1, len(nums)):
        if nums[write_index-1] != nums[i]:
            nums[write_index] = nums[i]
            write_index += 1
    return nums[:write_index]


print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]))
