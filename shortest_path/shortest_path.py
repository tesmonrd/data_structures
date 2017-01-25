# _*_ coing utf-8 _*_
"""A."""
# from graphtrav import breadth_first
from weight_graph import Graph
from collections import deque


def dijkstra(graph, start, end):
    """Calculate the shortest path."""
    g = Graph(graph)
    final = {}
    # all_visited = []
    visited, d = [], deque([start])
    while d:
        vertex = d.pop()
        visited.append(vertex)
        if g.neighbors(vertex):
            d.extend(g.neighbors(vertex))
            continue

        # FIND THE WEIGHT OF THIS PATH
        try:
            weight = 0
            for idx in range(len(visited)):
                weight += int(g.weight(visited[idx], visited[idx + 1]))
        except IndexError:
            pass

        path = list(visited)
        final[weight] = path

        #
        print(visited)
        try:
            print(d)
            for item in range(len(visited)):
                if g.neighbors(visited[-item - 1]) not in d:
                    visited.pop()
                else:
                    break
        except IndexError:
            pass
        print(visited)

        break
    print('################')
    # print('WEIGHT: ' + str(weight))
    # print('FINAL PATH: ' + str(path))
    print(final)


if __name__ == '__main__':
    graph = {'A': {'B': 15, 'C': 20},
             'B': {'C': 1},
             'C': {'D': 100, 'E': 2},
             'D': {'E': 11},
             'E': {}
             }
    dijkstra(graph, 'A', 'E')
