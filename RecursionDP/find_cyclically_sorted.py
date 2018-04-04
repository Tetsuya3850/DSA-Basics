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
print (find_cyclically_sorted(A, k))


def find_cyclically_sorted_nonu(A, k):
    def cyclically_sorted_helper(A, l, r, k):
        mid = (l + r) // 2
        if A[mid] == k:
            return mid
        if r < l:
            return False

        if A[l] < A[mid]:
            if k >= A[l] and k < A[mid]:
                return cyclically_sorted_helper(A, l, mid-1, k)
            else:
                return cyclically_sorted_helper(A, mid+1, r, k)
        elif A[mid] < A[l]:
            if k > A[mid] and k <= A[r]:
                return cyclically_sorted_helper(A, mid+1, r, k)
            else:
                return cyclically_sorted_helper(A, l, mid-1, k)
        elif A[l] == A[mid]:
            if A[mid] != A[r]:
                return cyclically_sorted_helper(A, mid+1, r, k)
            else:
                result = cyclically_sorted_helper(A, l, mid-1, k)
                if not result:
                    return cyclically_sorted_helper(A, mid+1, r, k)
                else:
                    return result
        return False

    return cyclically_sorted_helper(A, 0, len(A) - 1, k)

A = [2, 2, 2, 3, 4, 2]
k = 2
print (find_cyclically_sorted_nonu(A, k))
