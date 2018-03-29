from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)

    def path_BFS(self, start, end):
        visited = set()
        visited.add(start)
        queue = deque()
        queue.append((start, [start]))

        while queue:
            vertex, path = queue.popleft()
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    if neighbour == end:
                        return path + [neighbour]
                    queue.append((neighbour, path + [neighbour]))
                    visited.add(neighbour)

    def has_path_DFS(self, start, end):
        def has_path_DFS_helper(start, end):
            visited.add(start)
            if start == end:
                return True
            for neighbour in self.graph[start]:
                if neighbour not in visited:
                    if has_path_DFS_helper(neighbour, end):
                        return True
            return False

        visited = set()
        return has_path_DFS_helper(start, end)

    def isCyclic(self):
        def isCyclicUtil(v):
            visited.add(v)
            currRec.add(v)
            for neighbour in self.graph[v]:
                if not neighbour in visited:
                    if isCyclicUtil(neighbour):
                        return True
                elif neighbour in currRec:
                    return True
            currRec.remove(v)
            return False

        visited = set()
        currRec = set()
        for node in self.nodes:
            if node not in visited:
                if isCyclicUtil(node):
                    return True
        return False

    def toplogical_sort(self):
        def toplogical_sort_util(node):
            visited.add(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    toplogical_sort_util(neighbour)
            stack.append(node)

        if self.isCyclic():
            return False
        visited = set()
        stack = []
        for node in self.nodes:
            if node not in visited:
                toplogical_sort_util(node)
        return stack[::-1]

    def has_path_BFS_bidirectional(self, start, end):
        def BFS_once(queue, visited):
            vertex = queue.popleft()
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

        visited_1 = set()
        visited_2 = set()
        visited_1.add(start)
        visited_2.add(end)
        queue_1 = deque()
        queue_2 = deque()
        queue_1.append(start)
        queue_2.append(end)

        while queue_1 and queue_2:
            BFS_once(queue_1, visited_1)
            BFS_once(queue_2, visited_2)
            if visited_1 & visited_2:
                return True
        return False

g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'E')
g.addEdge('A', 'F')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('D', 'C')
g.addEdge('D', 'E')
print (g.path_BFS('A', 'D'))
print (g.has_path_DFS('A', 'D'))
print (g.isCyclic())
print (g.toplogical_sort())
print (g.has_path_BFS_bidirectional('A', 'D'))
