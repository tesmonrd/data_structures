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
        if n not in self.graph:
            self.graph[n] = []

    def add_edge(self, n1, n2):
        """Add edge between two nodes."""
        if n1 in self.graph:
            self.graph[n1].append(n2)
        if n2 not in self.graph:
            self.add_node(n2)
        self.graph.setdefault(n1, [n2])

    def del_node(self, n):
        """Delete a node."""
        if n in self.graph:
            del self.graph[n]
            for key, lst in self.graph.iteritems():
                if n in lst:
                    del lst[lst.index(n)]
        else:
            raise KeyError(u"Node does not exist!")

    def del_edge(self, n1, n2):
        """Delete an edge between two nodes."""
        if n1 in self.graph:
            if n2 in self.graph[n1]:
                self.graph[n1].remove(n2)
        else:
            raise KeyError(u"Edge does not exist!")

    def has_node(self, n):
        """Check if a node is in a dictionary."""
        print(n in self.graph)
        return n in self.graph

    def neighbors(self, n):
        """Check if node has neighbors."""
        if n in self.graph:
            return self.graph[n]
        else:
            raise KeyError(u"No Neighbors :(")

    def adjacent(self, n1, n2):
        """Return True if there is an edge between n1 & n2."""
        try:
            return n2 in self.graph[n1]
        except:
            raise KeyError(u"Node is not in dictionary!")


if __name__ == '__main__':
    g = Graph()
    g.add_node("A")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_node("A")
    # g.del_node("F")
    g.add_edge("B", "C")
    print(g.adjacent("B", "B"))
    # g.del_edge("P", "F")
    # print(g.edges())
