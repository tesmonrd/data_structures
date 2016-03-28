# _*_ coing utf-8 _*_
"""A."""
# from graphtrav import breadth_first
from weight_graph import Graph
from collections import deque


def dijkstra(graph, start, end):
    """Calculate the shortest path."""
    g = Graph(graph)
    # all_visited = []
    visited, d, weight = [], deque([start]), 0
    while d:
        vertex = d.pop()
        visited.append(vertex)
        if g.neighbors(vertex):
            d.extend(g.neighbors(vertex))
            continue

        # FIND THE WEIGHT OF THIS PATH
        try:
            idx = 0
            for item in visited:
                weight += int(g.weight(visited[idx], visited[idx + 1]))
                idx += 1
        except IndexError:
            pass


        break
    print('################')
    print('WEIGHT: ' + str(weight))
    print('FINAL PATH: ' + str(visited))


if __name__ == '__main__':
    graph = {'A': {'B': 15, 'C': 20},
             'B': {'C': 1},
             'C': {'D': 100, 'E': 2},
             'D': {'E': 11},
             'E': {}
             }
    dijkstra(graph, 'A', 'E')
