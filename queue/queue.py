class Node(object):
    """L."""

    def __init__(self, data, prev=None, next=None):
        """I."""
        self.data = data
        self.prev = prev
        self.next = next


class Queue(object):
    """S."""

    def __init__(self, head=None, tail=None, p=None):
        """Q."""
        self.head = head
        self.tail = tail
        self.p = p
        self.queue_size = 0

    def enqueue(self, data):
        """V."""
        if self.queue_size == 0:
            self.head = Node(data)
            self.tail = Node(data)
            self.queue_size += 1
            print(self.head.data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            print(new_node.prev.data)
            self.tail = new_node
            print(self.tail.data)
            print("****************")

    def size(self):
        """S."""
        pass


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
