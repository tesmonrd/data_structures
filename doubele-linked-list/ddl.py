# _*_ coding utf-8 _*_


class Node(object):
    """Node object."""

    def __init__(self, data, prev=None, next_node=None):
        """Initialize the Node."""
        self.data = data
        self.prev = prev
        self.next_node = next_node


class DoubleLink(object):
    """Class to work on node data."""

    def __init__(self):
        """Initialize the data structure."""
        self.head = None
        self.tail = None
        self.list = " "

    def insert(self, data):
        """Insert the node data as the new head."""
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.next_node = self.head
            self.head = new_node
        return(self.head.data)

    def append(self, data):
        """Append the node data as the new tail."""
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
        """Pop the head off the double linked list."""
        pop_val = self.head.data
        self.head = self.head.next_node
        print(pop_val)
        return pop_val

    def shift(self):
        """Shift the tail off the double linked list."""
        shift_val = self.tail.data
        self.tail = self.tail.prev
        return shift_val
        
    def remove(self, value):
        """Remove a given node from linked list."""
        target_node = value
        if target_node == self.head.data:
            self.pop()
        elif target_node == self.tail.data:
            self.shift()
        else:
            while self.head.next_node:
                try:
                    if self.head.next_node == target_node:
                        self.head.next_node = target_node.next_node
                        target_node = self.head.next_node
                        next_target = self.head.next_node
                        next_target.prev = self.head.prev
                        break
                    self.head = self.head.next_node
                except AttributeError:
                    pass
            else:
                raise AttributeError
        return target_node
