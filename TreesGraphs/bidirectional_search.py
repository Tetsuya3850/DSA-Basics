
from collections import defaultdict, deque


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

    def path_BFS_bidirectional(self, start, end):
        # Time O(k^q/2). Space O(k^q/2), where k is the avg num of edges per vertex and q is the length of path.
        class PathNode:
            def __init__(self, vertex, previous):
                self.vertex = vertex
                self.previous = previous

            def collapse(self, direction):
                def helper(pathNode):
                    if not pathNode:
                        return
                    nonlocal result
                    result.append(pathNode.vertex.name)
                    helper(pathNode.previous)
                result = []
                helper(self)
                if direction:
                    return result[::-1]
                else:
                    return result

        class BFSData:
            def __init__(self, root):
                self.queue = deque()
                self.visited = defaultdict()
                pathNode = PathNode(root, None)
                self.queue.append(pathNode)
                self.visited[root.name] = pathNode

            def is_finished(self):
                return not self.queue

        def searchLevel(primary, secondary):
            count = len(primary.queue)
            for _ in range(count):
                pathNode = primary.queue.popleft()
                if pathNode.vertex.name in secondary.visited:
                    return pathNode.vertex.name
                for neighbour in pathNode.vertex.adjacent:
                    if neighbour not in primary.visited:
                        next = PathNode(neighbour, pathNode)
                        primary.queue.append(next)
                        primary.visited[neighbour.name] = next
            return None

        def merge_paths(bfs1, bfs2, connection):
            end1 = bfs1.visited[connection]
            end2 = bfs2.visited[connection]
            return end1.collapse(True)[:-1] + end2.collapse(False)

        sourceData = BFSData(start)
        destData = BFSData(end)
        while not sourceData.is_finished() and not destData.is_finished():
            collision = searchLevel(sourceData, destData)
            if collision != None:
                return merge_paths(sourceData, destData, collision)
            collision = searchLevel(destData, sourceData)
            if collision != None:
                return merge_paths(sourceData, destData, collision)
        return None


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
print(g.path_BFS_bidirectional(a, d))
