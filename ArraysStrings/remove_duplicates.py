def remove_duplicates(nums):
    write_index = 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[write_index] = nums[i]
            write_index += 1
    nums[write_index] = nums[-1]
    write_index += 1
    return nums[:write_index]

print (removeDuplicates([1, 2, 2, 3, 4, 4, 4, 5, 5]))
