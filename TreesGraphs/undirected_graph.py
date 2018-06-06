
class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = []

    def addEdge(self, vertex):
        self.adjacent.append(vertex)
        vertex.adjacent.append(self)


class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def is_cyclic(self):
        def is_cyclic_util(vertex, visited, parent):
            visited.add(vertex)
            for neighbour in vertex.adjacent:
                if neighbour not in visited:
                    if is_cyclic_util(neighbour, visited, vertex):
                        return True
                elif neighbour != parent:
                    return True
            return False

        visited = set()
        for vertex in self.vertices:
            if vertex not in visited:
                if is_cyclic_util(vertex, visited, None):
                    return True
        return False

    def num_islands(self):
        def dfs(vertex, visited):
            visited.add(vertex)
            for neighbour in vertex.adjacent:
                if neighbour not in visited:
                    dfs(neighbour, visited)

        count = 0
        visited = set()
        for vertex in self.vertices:
            if vertex not in visited:
                dfs(vertex, visited)
                count += 1
        return count

    def is_tree(self):
        return self.num_islands() == 1 and not self.is_cyclic()
