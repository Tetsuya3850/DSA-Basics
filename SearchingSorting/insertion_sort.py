
def insertion_sort(A):
    # Time O(N^2), Space O(1), where N is the length of the array.
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


A = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(A))
