# _*_ coding: utf-8 _*_


class Graph(object):
    """A."""

    def __init__(self):
        """Initialize graph."""
        self.graph = {}

    def nodes(self):
        """List nodes in graph."""
        node_list = list(self.graph.keys())
        print(node_list)
        return node_list

    def edges(self):
        """List edges in graph."""
        return self.graph

    def add_node(self, n):
        """Add new node to the graph."""
        self.graph[n] = []
        return self.graph

    def add_edge(self, n1, n2):
        """Add edge between two nodes."""
        if n1 and n2 not in self.graph:
            self.graph.setdefault(n1, n2)
            self.add_node(n2)
        else:
            self.graph[n1] = n2





g = Graph()
g.add_node(1)
g.add_node(4)
g.nodes()
g.add_edge(1, 4)
print(g.graph)
