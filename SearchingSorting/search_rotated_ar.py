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


def find_cyclically_sorted(A, k):
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == k:
            return mid
        elif A[l] < A[mid]:
            if k >= A[l] and k < A[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if k > A[mid] and k <= A[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False


A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
k = 220
print(find_cyclically_sorted(A, k))
