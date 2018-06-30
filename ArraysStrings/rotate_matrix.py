
def rotate_matrix(matrix):
    # Time O(N^2), Space O(1), where N is the length of the side of the matrix.
    N = len(matrix)
    for offset in range(N // 2):
        for shift in range(N - offset*2 - 1):
            pos = shift+offset
            first = matrix[offset][pos]
            matrix[offset][pos] = matrix[N-1-pos][offset]
            matrix[N-1-pos][offset] = matrix[N-1-offset][N-1-pos]
            matrix[N-1-offset][N-1-pos] = matrix[pos][N-1-offset]
            matrix[pos][N-1-offset] = first
    return matrix


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
