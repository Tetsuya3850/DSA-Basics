
def sorted_matrix_search(A, m, n, k):
    # Given an M * N matrix in which each row and each column is sorted in ascending order,
    # write a method to find an element.
    # Time O(M+N), Space O(1), where M, N is the length of 2D array.
    row, col = 0, n-1
    while row <= m-1 and col >= 0:
        if A[row][col] == k:
            return True
        elif A[row][col] > k:
            col -= 1
        else:
            row += 1
    return False


A = [[2, 4, 7, 10], [3, 6, 9, 11], [5, 7, 10, 12]]
m = 3
n = 4
k = 9
print(sorted_matrix_search(A, m, n, k))
