def quick_sort(A):
    def quick_sort_helper(A, l, r):
        if l < r:
            pi = partition(A, l, r)
            quick_sort_helper(A, l, pi-1)
            quick_sort_helper(A, pi+1, r)

    def partition(A, l, r):
        pivot = A[r]
        i = l - 1
        for j in range(l, r):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i+1

    quick_sort_helper(A, 0, len(A)-1)
    return A

A = [64, 34, 25, 12, 22, 11, 90]
print (quick_sort(A))
