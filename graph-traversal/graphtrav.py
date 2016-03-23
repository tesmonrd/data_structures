# __ coding utf-8 __


from simple_graph import Graph
from collections import deque


def breadth_first(graph, start):
    """Depth First Traveral using a Deque as a Stack."""
    g = Graph(graph)
    visited, d = [], deque([start])
    while d:
        vertex = d.popleft()
        if vertex not in visited:
            visited.append(vertex)
            if visited not in g.neighbors(vertex):
                d.extend(g.neighbors(vertex))
    print(visited)
    return visited


if __name__ == "__main__":
    graph = {'A': ['B', 'C'], 'B': ['D', 'C'], 'C': [], 'D': ['E'], 'E': []}
    breadth_first(graph, 'A')
