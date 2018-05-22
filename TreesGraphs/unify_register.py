from collections import defaultdict


def baby_names(name_frequency, same_names):
    # Given two lists, one of names/frequencies and the other of pairs of equivalent names, write an algorithm to print a new list of the true frquency of each name.
    # Time O(B+P), where B is the num of babies and P is the pair of same names.
    g = Graph()
    for synonyms in same_names:
        g.addEdge(synonyms[0], synonyms[1])
    visited = set()
    unified_dict = defaultdict(int)
    for node in g.graph.keys():
        if node not in visited:
            unified_dict[node] = add_all_synonyms(
                node, visited, name_frequency, g)
    return unified_dict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.nodes.add(u)
        self.nodes.add(v)


def add_all_synonyms(vertex, visited, name_frequency, g, ):
    count = 0
    stack = []
    stack.append(vertex)
    visited.add(vertex)
    count += name_frequency[vertex]
    while stack:
        s = stack.pop()
        for neighbour in g.graph[s]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                count += name_frequency[neighbour]
    return count


name_frequency = defaultdict(int)
name_frequency['John'] = 15
name_frequency['Jon'] = 12
name_frequency['Chris'] = 13
name_frequency['Kris'] = 4
name_frequency['Christopher'] = 19

same_names = [("Jon", "John"), ("John", "Johnny"),
              ("Chris", "Kris"), ("Kris", "Christopher")]

print(baby_names(name_frequency, same_names))
