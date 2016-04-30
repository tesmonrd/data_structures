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
        self.count = 0

    def append(self, val):
        """Add values to the end of deque."""
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return self.tail.data

    def appendleft(self, val):
        """Add values to the front of the deque."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
        return self.head.data

    def pop(self):
        """Remove a value from the end of the deque and returns it."""
        try:
            pop_value = self.tail.data
            self.tail = self.tail.prev
            self.count -= 1
            return pop_value
        except AttributeError:
            raise AttributeError("No items in deque!")

    def popleft(self):
        """Remove a value from the front of the deque and returns it."""
        try:
            pop_left_value = self.head.data
            self.head = self.head.next
            self.count -= 1
            return pop_left_value
        except AttributeError:
            raise AttributeError("No items in deque!")

    def peek(self):
        """Return the next value that would be returned by pop."""
        if self.count <= 1:
            return None
        else:
            return self.tail.prev.data

    def peekleft(self):
        """Return the next value that is returned by popleft."""
        if self.count <= 1:
            return None
        else:
            return self.head.next.data

    def size(self):
        """Return the size of the deque."""
        return self.count
