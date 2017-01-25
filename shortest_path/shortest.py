from weight_graph import Graph
from itertools import count
from heapq import heappop, heappush


def dijkstra(graph, start, target):
    unique = count()
    visited = set()
    heap = [(0, unique, start, ())]
    while heap:
        weight, junk, node, path = heappop(heap)
        if node == target:
            return weight, path
        if node not in visited:
            visited.add(node)
            for neighbor, edge in graph[node].items():
                heappush(heap, (weight + edge, next(unique),
                         neighbor, (neighbor, path)))


if __name__ == '__main__':
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 20)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 200)

    dijkstra(g, 'A', 'D')
