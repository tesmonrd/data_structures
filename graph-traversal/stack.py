# _*_UTF-8 _*_
"""Implements a Stack using Python without built-ins given value(s)."""


class Node(object):
    """Node for individual stack items."""

    def __init__(self, item):
        """Initialize the node."""
        self.item = item
        self.next = None


class Stack(object):
    """Constructor class for the Stack module."""

    def __init__(self):
        """Initialize the Stack."""
        self.head = None
        self.count = 0

    def size(self):
        """Track the count of items in Stack."""
        return self.count

    def push(self, value):
        """Add a value into the stack from the top position."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return new_node.item

    def empty(self):
        """Create a True/False condition for pop if nothing in stack."""
        return self.count == 0

    def pop(self):
        """Pop the value from the Stack."""
        if not None:
            new_node = self.head
            self.head = new_node.next
            self.count -= 1
            return self.head.item
        else:
            raise ValueError
