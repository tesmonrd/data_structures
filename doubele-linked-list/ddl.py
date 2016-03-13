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
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.next_node = self.head
            self.head = new_node
        # self.list += "({})"format(str(self.head.data)) + ", "
        return(self.head.data)

    def append(self, data):
        """D."""
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node
        self.list += str(self.tail.data) + ", "
        return(self.tail.data)

    def pop(self):
        """E."""
        pop_val = self.head.data
        self.head = self.head.next_node
        print(pop_val)
        return pop_val

    def shift(self):
        """F."""
        shift_val = self.tail.data
        self.tail = self.tail.prev
        return shift_val

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
