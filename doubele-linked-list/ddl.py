# _*_ coding utf-8 _*_


class Node(object):
    """A."""

    def __init__(self, data, prev=None, next_node=None):
        """A."""
        self.data = data
        self.prev = prev
        self.next_node = next_node


class DoubleLink(object):
    """B."""

    def __init__(self):
        """B."""
        self.head = None
        self.tail = None
        self.list = " "

    def insert(self, data):
        """C."""
        if self.head is None:
            self.head = Node(data)
            self.tail = Node(data)
        else:
            new_node = Node(data, prev=self.head)
            self.head.next_node = new_node
            self.head = new_node
        self.list += str(self.head.data) + ", "

    def append(self, data):
        """D."""
        if self.tail is None:
            self.tail = Node(data)
            self.head = Node(data)
        else:
            new_node = Node(data, next_node=self.tail)
            self.tail.prev = new_node
            self.tail = new_node
        self.list += str(self.tail.data) + ", " 

    def pop(self):
        """E."""
        self.head = self.head.prev
        self.head.next_node = None
        return self.head.next_node

    def shift(self):
        """F."""
        self.tail = self.tail.next_node
        self.tail.prev = None
        return self.tail.prev

    def remove(self, data):
        """G."""
        current = self.head
        try:
            hip = True
            while hip is True:
                if current == data:
                    current.next_node.prev = current.prev
                    current.prev.next_node = current.next_node
                    current.next_node = None
                    current.prev = None
                    hip = False
                    break
                current = current.prev
                continue
        except:
            raise IndexError

    def display(self):
        """H."""
        print("(" + self.list + ")")


dl = DoubleLink()
dl.insert("2")
dl.append("1")
dl.insert("4")
dl.append("3")
dl.display()
