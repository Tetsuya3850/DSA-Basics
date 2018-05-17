
def selection_sort(A):
    # Time O(N^2), Space O(1), where N is the length of the array.
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
    return A


A = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(A))
