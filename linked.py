#  _*_ coding utf-8 _*_
"""LINKED LIST."""


class Node(object):
    """Node establishes functions that move within the list."""

    def __init__(self, value, next=None):
        """Initialize the list."""
        self.value = value
        self.next = next


class LinkedList(object):
    """Manipulate the linked list."""

    def __init__(self):
        """Initialize the head of the node to (None is not given)."""
        self.head = None
        self.size = 0
        self.result = u""

    def insert(self, value):
        """Insert new node."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.result += str(new_node.value)
        else:
            new_node.next = self.head
            self.head = new_node
            self.result += u", " + str(new_node.value)
        self.size += 1
        return new_node.value

    def pop(self):
        """The method will pop off the head of the node."""
        current = self.head
        self.head = self.head.next
        self.size -= 1
        return current.value

    def get_size(self):
        """Get the total count of nodes in list."""
        return self.size

    def search(self, value):
        """Search for a specific node in list."""
        current = self.head
        while current and True:
            if current.value == value:
                break
            else:
                current = current.next
        if current is None:
            raise ValueError(u"Data not in List")
        return current.value

    def remove(self, value):
        """Remove a specific node in list."""
        current = self.head
        previous_node = None
        found = False
        while current and found is False:
            if current.value == value:
                found = True
                self.size -= 1
            else:
                previous_node = current
                current = current.next
        if current is None:
            raise ValueError(u"Data is not present in list!")
        if previous_node is None:
            self.head = current.next
        return current.value

    def display(self):
        """Display the list."""
        print(u"(" + self.result + u")")
