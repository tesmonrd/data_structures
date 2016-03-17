# _*_ coding: utf-8 _*_


class Graph(object):
    """A."""

    def __init__(self):
        """Initialize graph."""
        self.graph = {}

    def nodes(self):
        """List nodes in graph."""
        node_list = list(self.graph.keys())
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
            self.graph.setdefault(n1, [n2])
            self.add_node(n2)
        else:
            self.graph[n1].append(n2)

    def del_node(self, n):
        """Delete a node."""
        if n in self.graph:
            del self.graph[n]
        else:
            raise KeyError("Node not in graph!")

    def del_edge(self, n1, n2):
        """Delete an edge between two nodes."""
        if n1 in self.graph:
            if n2 in self.graph[n1]:
                self.graph[n1].remove(n2)
        else:
            raise IndexError("Edge does not exist!")

    def has_node(self, n):
        """Check if a node is in a dictionary."""
        if n in self.graph:
            print("TRUE")
            return True
        else:
            print("FALSE")
            return False


g = Graph()
g.add_node(1)
g.add_node(4)
g.add_node(8)
g.add_node(4)
g.add_node(2)
g.add_node(10)
g.nodes()
g.add_edge(8, 4)
g.add_edge(1, 4)
g.add_edge(1, 8)
g.add_edge(2, 8)
print(g.graph)
g.del_edge(1, 8)
g.has_node(100)
g.has_node(8)
g.has_node(124)
g.has_node(4)
g.has_node(132)
g.has_node(2)

