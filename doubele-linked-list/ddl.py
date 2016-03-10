# _*_ coding utf-8 _*_


class Node(object):
    """Node Class."""

    def __init__(self, data, prev=None, next_node=None):
        """Instantiate a node."""
        self.data = data
        self.prev = prev
        self.next_node = next_node


class DoubleLink(object):
    """DLL Class."""

    def __init__(self):
        """Instantiate a head, tail, empty list and list size increment."""
        self.head = None
        self.tail = None
        self.list = " "
        self.size = 0

    def insert(self, data):
        """Insert a node to the head of list."""
        if self.head is None:
            self.head = Node(data)
            self.tail = Node(data)
        else:
            new_node = Node(data, prev=self.head)
            self.head.next_node = new_node
            self.head = new_node
        if len(self.list) == 1:
            self.list += str(self.head.data)
        else:
            self.list += ", " + str(self.head.data)
        self.size += 1
        return (self.head.data)

    def append(self, data):
        """Append a node to the tail of list."""
        if self.tail is None:
            self.tail = Node(data)
            self.head = Node(data)
        else:
            new_node = Node(data, next_node=self.tail)
            self.tail.prev = new_node
            self.tail = new_node
        if len(self.list) == 1:
            self.list += str(self.tail.data)
        else:
            self.list += ", " + str(self.tail.data)
        self.size += 1
        return (self.tail.data)

    def pop(self):
        """Point the head node one back from the current head node."""
        self.head = self.head.prev
        self.head.next_node = None
        # lst = self.list.split(", ")
        # for i in range(0, 2):
        #     lst.pop()
        # self.list = " "
        # for idx in lst:
        #     self.list += str(idx) + ", "
        # self.size -= 1
        # print(self.list)
        return self.list

    def shift(self):
        """Point the tail node one forward from the current tail node."""
        self.tail = self.tail.next_node
        self.tail.prev = None
        # lst = self.list.split(", ")
        # for i in range(0, 2):
        #     lst.pop(0)
        # self.list = ""
        # for idx in lst:
        #     self.list += str(idx) + ", "
        # self.size -= 1
        # print(self.list)
        return self.tail.prev

    def remove(self, data):
        """Increment through the list from the head to the tail.
        If the data in the node matches the node you want to remove.
        Then remove it!
        """
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

# The commented out code in pop() and shift() is a fail safe
