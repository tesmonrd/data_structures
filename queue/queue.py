class Node(object):
    """Node class."""

    def __init__(self, data, prev=None, next=None):
        """Instanitiate the Node class."""
        self.data = data
        self.prev = prev
        self.next = next


class Queue(object):
    """Quese data structure."""

    def __init__(self, head=None, tail=None, p=None):
        """Instanitiate the Queue class."""
        self.head = head
        self.tail = tail
        # self.p = p
        self.queue_size = 0

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
            # self.head.prev = self.head
            self.queue_size += 1
            print(self.head.data)
            # print(self.head.prev.data)
            print(new_node.prev.data)
            print(self.tail.data)
            print("****************")

    def size(self):
        """Size of Queue."""
        return self.queue_size

    def dequeue(self):
        """Remove the correct item from the queue."""
        print("You've removed: " + str(self.head.data) + " from the Queue")
        new_node = self.head
        print(new_node.data)
        new_node = new_node.prev
        print(new_node.data)
        new_node = self.head.prev
        print(new_node.data)

        # self.queue_size -= 1
        # if
        # print(self.head.data)
        print("****************")

    def peek(self, data):
        """Return next value in queue w/o dequeueing."""
        pass

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.dequeue()
