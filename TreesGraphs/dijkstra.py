from collections import defaultdict
from heapq import heappush, heappop

class WeightedVertex:
    def __init__(self, name):
        self.name = name
        self.adjacent = []

    def addEdge(self, vertex, weight):
        self.adjacent.append((vertex, weight))
        vertex.adjacent.append((self, weight))

class WeightedGraph:
    def __init__(self):
        self.vertexes = []

    def addVertex(self, vertex):
        self.vertexes.append(vertex)

    def dijkstra(self, s):
        heap = []
        heappush(heap, (0, s))
        path_dist = defaultdict()
        for vertex in self.vertexes:
            path_dist[vertex.name] = (float('inf'), [])
        path_dist[s.name] = (0, [s.name])
        while heap:
            dist, vertex = heappop(heap)
            for neighbour, weight in vertex.adjacent:
                next_distance = path_dist[vertex.name][0] + weight
                if path_dist[neighbour.name][0] > next_distance:
                    path_dist[neighbour.name] = (next_distance, path_dist[vertex.name][1] + [neighbour.name])
                    heappush(heap, (next_distance, neighbour))
        return path_dist

gr = WeightedGraph()
a = WeightedVertex('A')
b = WeightedVertex('B')
c = WeightedVertex('C')
d = WeightedVertex('D')
e = WeightedVertex('E')
f = WeightedVertex('F')
g = WeightedVertex('G')
h = WeightedVertex('H')
i = WeightedVertex('I')
a.addEdge(b, 4)
a.addEdge(h, 8)
b.addEdge(c, 8)
b.addEdge(h, 11)
c.addEdge(d, 7)
c.addEdge(f, 4)
c.addEdge(i, 2)
d.addEdge(e, 9)
d.addEdge(f, 14)
e.addEdge(f, 10)
f.addEdge(g, 2)
g.addEdge(h, 1)
g.addEdge(i, 6)
h.addEdge(i, 7)
gr.addVertex(a)
gr.addVertex(b)
gr.addVertex(c)
gr.addVertex(d)
gr.addVertex(e)
gr.addVertex(f)
gr.addVertex(g)
gr.addVertex(h)
gr.addVertex(i)
print (gr.dijkstra(a))
