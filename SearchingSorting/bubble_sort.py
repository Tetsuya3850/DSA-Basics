
def bubble_sort(A):
    # Time complexity O(N^2) Space complexity O(1)
    is_sorted = False
    last_unsorted = len(A) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(last_unsorted):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                is_sorted = False
        last_unsorted -= 1
    return A


A = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(A))
