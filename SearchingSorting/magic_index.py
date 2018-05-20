# Find a magic index, such that A[i] = i, given a sorted array of integers.


def magic_index(A):
    # Time O(N), Space O(1), where N is the length of the array.
    start, end = 0, len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == mid:
            return mid
        elif A[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1


A = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_index(A))


def magic_index_nonunique(A):
    def magic_index_helper(A, start, end):
        if end < start:
            return False
        midIndex = (start + end) // 2
        midValue = A[midIndex]
        if midIndex == midValue:
            return midIndex
        leftIndex = min(midIndex - 1, midValue)
        left = magic_index_helper(A, start, leftIndex)
        if left:
            return left
        rightIndex = max(midIndex + 1, midValue)
        right = magic_index_helper(A, rightIndex, end)
        return right

    return magic_index_helper(A, 0, len(A) - 1)


A = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(magic_index_nonunique(A))
