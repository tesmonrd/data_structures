"""DATA STRUCTURE - QUEUE."""


class Node(object):
    """Node class."""

    def __init__(self, data, prev=None, next=None):
        """Instanitiate the Node class."""
        self.data = data
        self.prev = prev
        self.next = next


class Queue(object):
    """Queue data structure."""

    def __init__(self, head=None, tail=None):
        """Instanitiate the Queue class."""
        self.head = head
        self.tail = tail
        self.queue_size = 0

    def size(self):
        """Size of Queue."""
        return self.queue_size

    def enqueue(self, data):
        """Add the value to the queue."""
        if self.queue_size == 0:
            self.head = Node(data)
            self.tail = Node(data)
            self.queue_size += 1
        else:
            new_node = Node(data, self.head)
            new_node.prev = self.tail
            self.tail = new_node

    def dequeue(self):
        """Remove the correct item from the queue."""
        removed_tail = self.tail
        self.tail = self.tail.prev
        self.queue_size += 1
        return removed_tail.data

    def peek(self):
        """Return next value in queue w/o dequeueing."""
        try:
            return self.tail.prev.data
        except AttributeError:
            return None
