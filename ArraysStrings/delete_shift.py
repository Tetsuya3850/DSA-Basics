

def array_key_delete(A, k):
    # Delete all instances of int k from int array, in-place.
    # Time O(N), Space O(1), where N is the length of the array.
    write_index = 0
    for i in range(len(A)):
        if A[i] != k:
            A[write_index] = A[i]
            write_index += 1
    return A[:write_index]


print(array_key_delete([3, 11, 2, 3, 3, 7, 13, 3], 3))


def remove_duplicates(nums):
    # Remove all duplicate ints and make the elements unique, in-place.
    # Time O(N), Space O(1), where N is the length of the array.
    write_index = 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[write_index] = nums[i]
            write_index += 1
    nums[write_index] = nums[-1]
    write_index += 1
    return nums[:write_index]


print(remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5, 5]))
