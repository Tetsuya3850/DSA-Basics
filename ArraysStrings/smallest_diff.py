
def smallest_diff(A, B):
    # Time O(A+B), Space O(1), where A is the length of the array A and B is the length of the array B.
    i, j = 0, 0
    smallest = float('inf')
    while i < len(A) and j < len(B):
        smallest = min(smallest, abs(A[i] - B[j]))
        if A[i] <= B[j]:
            i += 1
        else:
            j += 1
    return smallest


print(smallest_diff([0, 4, 8, 13], [2, 9]))
