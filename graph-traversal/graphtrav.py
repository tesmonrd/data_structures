# __ coding utf-8 __
"""Implement graph traversal."""

from simple_graph import Graph
from collections import deque


def breadth_first(graph, start):
    """Breadth First Traveral using a Deque as a queue."""
    g = Graph(graph)
    visited, d = [], deque([start])
    while d:
        vertex = d.popleft()
        if vertex not in visited:
            visited.append(vertex)
            if visited not in g.neighbors(vertex):
                d.extend(g.neighbors(vertex))
    return visited


def depth_first(graph, start):
    """Depth first traversal using deque as a stack."""
    g = Graph(graph)
    visited, d = [], deque([start])
    while d:
        vertex = d.pop()
        if vertex not in visited:
            visited.append(vertex)
            if visited not in g.neighbors(vertex):
                d.extend(g.neighbors(vertex))
    return(visited)

if __name__ == "__main__":
    graph = {'A': ['B', 'C', 'Q'],
             'B': ['C', 'E'],
             'C': ['D'],
             'D': ['Q'],
             'E': [],
             'Q': ['B']
             }
    breadth_first(graph, 'A')
    depth_first(graph, 'A')
