def n_queens(n):
    # Write a program which returns all distinct nonattacking placements of n queens on an n * n chessboard, where n is an input to the program.

    def n_queens_helper(row):
        if row == n:
            print(columns)
            return
        for col in range(n):
            if check_valid(columns, row, col):
                columns[row] = col
                n_queens_helper(row + 1)

    def check_valid(columns, row, col):
        for i in range(row):
            if columns[i] == col:
                return False
        for j in range(1, row + 1):
            if abs(col - columns[row - j]) == j:
                return False
        return True

    columns = [None] * n
    n_queens_helper(0)


n_queens(4)
