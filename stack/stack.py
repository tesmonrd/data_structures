# _*_UTF-8 _*_


class Node(object):
    """A ."""

    def __init__(self, item):
        """A ."""
        self.item = item
        self.next = None


class Stack(object):
    """A ."""

    def __init__(self):
        """B ."""
        self.head = None

    def push(self, value):
        """C ."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(new_node.item)
        return new_node.item

s = Stack()
s.push(4)
