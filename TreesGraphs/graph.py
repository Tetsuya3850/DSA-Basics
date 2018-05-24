from collections import defaultdict, deque, Counter


class Vertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = []

    def addEdge(self, vertex):
        self.adjacent.append(vertex)


class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def path_BFS(self, start, end):
        # Time O(k^q). Space O(k^q), where k is the avg num of edges per vertex and q is the length of path.
        queue = deque()
        queue.append((start, [start.name]))
        visited = set()
        visited.add(start)
        while queue:
            vertex, path = queue.popleft()
            for neighbour in vertex.adjacent:
                if neighbour not in visited:
                    if neighbour == end:
                        return path + [neighbour.name]
                    queue.append((neighbour, path + [neighbour.name]))
                    visited.add(neighbour)

    def has_path_DFS(self, start, end):
        def has_path_DFS_helper(start, end):
            visited.add(start)
            if start == end:
                return True
            for neighbour in start.adjacent:
                if neighbour not in visited:
                    if has_path_DFS_helper(neighbour, end):
                        return True
            return False

        visited = set()
        return has_path_DFS_helper(start, end)

    def isCyclic(self):
        # Time O(V + E), Space O(V), where V is the num of vertices and E is the num of edges.
        def isCyclicUtil(v):
            visited.add(v)
            currRec.add(v)
            for neighbour in v.adjacent:
                if not neighbour in visited:
                    if isCyclicUtil(neighbour):
                        return True
                elif neighbour in currRec:
                    return True
            currRec.remove(v)
            return False

        visited = set()
        currRec = set()
        for vertex in self.vertices:
            if vertex not in visited:
                if isCyclicUtil(vertex):
                    return True
        return False

    def toplogical_sort(self):
        # Time O(V + E), Space O(V+E), where V is the num of vertices and E is the num of edges.
        def inbound_count():
            c = Counter()
            for vertex in self.vertices:
                c[vertex] = 0
            for vertex in self.vertices:
                for neighbour in vertex.adjacent:
                    c[neighbour] += 1
            return c

        def add_non_dependent(inbound_counter, process_next):
            add = []
            for key, value in inbound_counter.items():
                if value == 0:
                    add.append(key)
            for vertex in add:
                del inbound_counter[vertex]
            process_next.extend(add)

        order = []
        process_next = deque()
        inbound_counter = inbound_count()
        add_non_dependent(inbound_counter, process_next)
        while process_next:
            vertex = process_next.popleft()
            for neighbour in vertex.adjacent:
                inbound_counter[neighbour] -= 1
            order.append(vertex.name)
            add_non_dependent(inbound_counter, process_next)
        return order if len(order) == len(self.vertices) else 'Cycle!'

    def toplogical_sort_alternative(self):
        # Time O(V + E), Space O(V), where V is the num of vertices and E is the num of edges.
        def toplogical_sort_util(v, stack):
            visited.add(v)
            for neighbour in v.adjacent:
                if neighbour not in visited:
                    toplogical_sort_util(neighbour, stack)
            stack.append(v.name)

        if self.isCyclic():
            return False
        visited = set()
        stack = []
        for vertex in self.vertices:
            if vertex not in visited:
                toplogical_sort_util(vertex, stack)
        return stack[::-1]

    def has_path_BFS_bidirectional(self, start, end):
        # Time O(k^q/2). Space O(k^q/2), where k is the avg num of edges per vertex and q is the length of path.
        def BFS_once(queue, visited):
            vertex = queue.popleft()
            for neighbour in vertex.adjacent:
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
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
f = Vertex('F')
a.addEdge(b)
a.addEdge(e)
a.addEdge(f)
b.addEdge(d)
b.addEdge(e)
d.addEdge(c)
d.addEdge(e)
g.addVertex(a)
g.addVertex(b)
g.addVertex(c)
g.addVertex(d)
g.addVertex(e)
g.addVertex(f)
print(g.path_BFS(a, d))
print(g.has_path_DFS(a, d))
print(g.isCyclic())
print(g.toplogical_sort())
print(g.toplogical_sort_alternative())
print(g.has_path_BFS_bidirectional(a, d))
