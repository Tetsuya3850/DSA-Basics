
def maze_solver(A, start, end):
    def isSafe(A, r, c):
        return r < len(A) and c < len(A[0]) and A[r][c]

    def maze_solver_helper(A, r, c, path):
        if r == len(A) - 1 and c == len(A[0]) - 1:
            path[r][c] = 1
            return True
        if isSafe(A, r, c):
            path[r][c] = 1
            if maze_solver_helper(A, r+1, c, path):
                return True
            if maze_solver_helper(A, r, c+1, path):
                return True
            path[r][c] = 0
        return False

    path = [[0 for j in range(4)] for i in range(4)]
    if maze_solver_helper(A, 0, 0, path):
        return path
    else:
        return 'No path!'


A = [[1, 1, 1, 1], [1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1]]
print(maze_solver(A, 0, 0))


def get_path(maze):
    def helper(maze, row, col, path, failed_points):
        if row < 0 or col < 0 or maze[row][col] == 0:
            return False
        if (row, col) in failed_points:
            return False
        if (row == 0 and col == 0) or helper(maze, row, col-1, path, failed_points) or helper(maze, row-1, col, path, failed_points):
            path.append((row, col))
            return True
        failed_points.add((row, col))
        return False

    path = []
    failed_points = set()
    if helper(maze, len(maze)-1, len(maze[0])-1, path, failed_points):
        return path
    else:
        return 'No path!'


print(get_path(A))
