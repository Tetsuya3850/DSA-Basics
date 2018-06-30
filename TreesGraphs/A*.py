
import heapq


class Cell:
    def __init__(self, r, c, wall):
        self.wall = wall
        self.r = r
        self.c = c
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0


class AStar:
    def __init__(self, start, end):
        self.opened = []
        self.closed = set()
        self.grid_height = 6
        self.grid_width = 6
        self.cells = []
        self.init_grid(start, end)

    def init_grid(self, start, end):
        walls = ((0, 0), (0, 1), (0, 3), (1, 4), (2, 2),
                 (3, 3), (4, 1), (4, 3), (4, 4), (4, 5), (5, 1))
        for r in range(self.grid_height):
            for c in range(self.grid_width):
                if (r, c) in walls:
                    wall = True
                else:
                    wall = False
                self.cells.append(Cell(r, c, wall))
        self.start = self.get_cell(*start)
        self.end = self.get_cell(*end)

    def get_heuristic(self, cell):
        return abs(cell.r - self.end.r) + abs(cell.c - self.end.c)

    def get_cell(self, r, c):
        return self.cells[r * self.grid_height + c]

    def get_adjacent_cells(self, cell):
        cells = []
        if cell.r > 0:
            cells.append(self.get_cell(cell.r-1, cell.c))
        if cell.r < self.grid_height-1:
            cells.append(self.get_cell(cell.r+1, cell.c))
        if cell.c > 0:
            cells.append(self.get_cell(cell.r, cell.c-1))
        if cell.c < self.grid_width-1:
            cells.append(self.get_cell(cell.r, cell.c+1))
        return cells

    def get_path(self):
        cell = self.end
        path = [(cell.r, cell.c)]
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.r, cell.c))

        path.append((self.start.r, self.start.c))
        path.reverse()
        return path

    def update_cell(self, adj, cell):
        adj.g = cell.g + 1
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def solve(self):
        heapq.heappush(self.opened, (self.start.f, self.start))
        while self.opened:
            f, cell = heapq.heappop(self.opened)
            self.closed.add(cell)
            if cell is self.end:
                return self.get_path()
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if not adj_cell.wall and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        if adj_cell.g > cell.g + 1:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))


A = AStar((0, 5), (5, 0))
A.solve()
print(A.get_path())
