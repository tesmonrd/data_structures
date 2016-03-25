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
        lst = (list(self.graph.values()))
        edge_list = []
        for i in lst:
            if i != []:
                edge_list.extend(i)
        return edge_list

    def add_node(self, n):
        """Add new node to the graph."""
        self.graph[n] = {}
        return self.graph

    def add_edge(self, n1, n2, weight=0):
        """Add edge between two nodes."""
        if n1 in self.graph:
            self.graph[n1].setdefault(n2, weight)
        else:
            self.graph.setdefault(n1, {n2: weight})
            self.add_node(n2)

    def del_node(self, n):
        """Delete a node."""
        if n in self.graph:
            del self.graph[n]
            return self.graph
        else:
            raise KeyError(u"Node not in graph!")

    def del_edge(self, n1, n2):
        """Delete an edge between two nodes."""
        if n1 in self.graph:
            if n2 in self.graph[n1]:
                self.graph[n1].pop(n2)
                return self.graph
        else:
            raise IndexError(u"Edge does not exist!")

    def has_node(self, n):
        """Check if a node is in a dictionary."""
        if n in self.graph:
            print("True")
            return True
        else:
            print("False")
            return False

    def neighbors(self, n):
        """Check if node has neighbors."""
        if n in self.graph:
            return self.graph[n]
        else:
            raise IndexError(u"No Neighbors :(")

    def adjacent(self, n1, n2):
        """Return True if there is an edge between n1 & n2."""
        try:
            if n2 in self.graph[n1]:
                print("True")
                return True
            else:
                print("False")
                return False
        except:
            raise KeyError(u"Node is not in dictionary!")


g = Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(20, 16)
g.add_edge(20, 400)
g.del_edge(20, 400)
g.del_edge(20, 16)
