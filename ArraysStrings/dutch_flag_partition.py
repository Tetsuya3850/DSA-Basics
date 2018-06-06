
def dutch_flag_partition(index, A):
    # Time O(N), Space O(1), where N is the length of the array.
    pivot = A[index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    return A


print(dutch_flag_partition(1, [0, 1, 2, 1, 0, 0, 1]))
