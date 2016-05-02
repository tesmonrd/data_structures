# _*_ coding: utf-8 _*_
"""Graph Data Structure."""


class Graph(object):
    """Class of the Graph Data Structure."""

    def __init__(self):
        """Initialize graph."""
        self.graph = {}

    def nodes(self):
        """List nodes in graph."""
        return list(self.graph.keys())

    def edges(self):
        """List edges in graph."""
        edge_list = [(key, value) for key in self.graph for value in self.graph[key]]
        return edge_list

    def add_node(self, n):
        """Add new node to the graph."""
        self.graph[n] = []

    def add_edge(self, n1, n2):
        """Add edge between two nodes."""
        self.graph.setdefault(n1, []).append(n2)
        if n2 not in self.graph:
            self.graph.setdefault(n2, [])

    def del_node(self, n):
        """Delete a node."""
        if n in self.graph:
            del self.graph[n]
        else:
            print("Node not in graph!")

    def del_edge(self, n1, n2):
        """Delete an edge between two nodes."""
        try:
            self.graph[n1].remove(n2)
        except KeyError:
            raise KeyError(u"The key does not exist")
        except ValueError:
            raise ValueError(u"Edge does not exist!")

    def has_node(self, n):
        """Check if a node is in a dictionary."""
        if n in self.graph:
            return True
        else:
            return False

    def neighbors(self, n):
        """Check if node has neighbors."""
        try:
            return self.graph[n]
        except KeyError:
            raise KeyError(u"No Neighbors :(")

    def adjacent(self, n1, n2):
        """Return True if there is an edge between n1 & n2."""
        if self.has_node(n1) and self.has_node(n2):
            return n2 in self.graph[n1]

g = Graph()
g.add_node(2)
g.add_node(3)
# g.add_node(11)
# g.add_node(22)
g.add_edge(2, 3)

# g.add_edge(5, 100)
# g.add_edge(55, 5)
# print(g.neighbors(5))
# print(g.adjacent(11, 5))
# print(g.edges())
print(g.graph)
