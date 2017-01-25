#  _*_ coding utf-8 _*_


class Node(object):
    """Node establishes functions that move within the list."""

    def __init__(self, data=None, next_node=None):
        """Initialize the list."""
        self.data = data
        self.next_node = next_node

    def find_data(self):
        """Return the data."""
        return self.data

    def find_next_node(self):
        """Return the next node."""
        return self.next_node

    def set_next_node(self, new_next):
        """Reset next node."""
        self.next_node = new_next


class LinkedList(object):
    """Manipulate the linked list."""

    def __init__(self):
        """Initialize the head of the node to (None is not given)."""
        self.head = None
        self.size = 0

    def insert_node(self, data):
        """Insert new node."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1

    def get_size(self):
        """Get the total count of nodes in list."""
        return self.size

    def search(self, data):
        """Search for a specific node in list."""
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.find_data() == data:
                found = True
            else:
                current_node = current_node.find_next_node()
        if current_node is None:
            raise ValueError("Data not in List")
        return current_node

    def remove_node(self, data):
        """Remove a specific node in list."""
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found is False:
            if current_node.find_data() == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.find_next_node()
        if current_node is None:
            raise ValueError("Data is not present in list!")
        if previous_node is None:
            self.head = current_node.find_next_node()
        else:
            previous_node.remove(current_node)

    def display(self):
        """Display the list."""
        node_list = []
        node = self.head
        if node is not None:
            while node.next_node is not None:
                node_list.append(node.data)
                node = node.next_node
            node_list.append(node.data)
        print("({})".formati(inode_list)


mylist = LinkedList()
mylist.insert_node(1)
mylist.insert_node(2)
mylist.insert_node(3)

mylist.display()
