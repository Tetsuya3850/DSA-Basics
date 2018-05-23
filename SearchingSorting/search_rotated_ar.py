def search_rotated_ar(nums, target):
    # Time O(logN), Space O(1), where N is the length of the array.
    def helper(nums, target, left, right):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if right < left:
            return -1

        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                return helper(nums, target, left, mid-1)
            else:
                return helper(nums, target, mid+1, right)
        elif nums[left] > nums[mid]:
            if nums[mid] < target <= nums[right]:
                return helper(nums, target, mid+1, right)
            else:
                return helper(nums, target, left, mid-1)
        elif nums[left] == nums[mid]:
            if nums[mid] != nums[right]:
                return helper(nums, target, mid+1, right)
            else:
                result = helper(nums, target, left, mid-1)
                if result == -1:
                    return helper(nums, target, mid+1, right)
                else:
                    return result
        return -1

    return helper(nums, target, 0, len(nums)-1)


print(search_rotated_ar([4, 5, 6, 7, 0, 1, 2], 5))
