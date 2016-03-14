# _*_ utf-8 _*_
"""Deque Data Structure."""


class Node(object):
    """Node class."""

    def __init__(self, data, next=None, prev=None):
        """Instantiate the node class."""
        self.data = data
        self.next = next
        self.prev = prev


class Deque(object):
    """Deque class."""

    def __init__(self, head=None, tail=None):
        """Instantiate the deque class."""
        self.head = head
        self.tail = tail
        self.size = 0

    def append(self, val):
        """Add values to the end of deque."""
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.prev = new_node
            new_node.next = self.tail.prev
            self.tail = new_node
        self.size += 1
        return self.tail.data

    def appendleft(self, val):
        """Add values to the front of the deque."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.next = new_node
            new_node.prev = self.head.next
            self.head = new_node
        self.size += 1
        return self.head.data

    def pop(self):
        """Remove a value from the end of the deque and returns it."""
        pass

    def popleft(self):
        """Remove a value from the front of the deque and returns it."""
        pass

    def peek(self):
        """Return the next value that would be returned by pop."""
        pass

    def peekleft(self):
        """Return the next value that is returned by popleft."""
        pass

    def size(self):
        """Return the size of the deque."""
        return self.size
