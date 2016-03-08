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
    head = None

    def __init__(self, head):
        """Initialize the head of the node to (None is not given)."""
        self.head = head
        self.size = 0

    def get_size(self):
        """Get the total count of nodes in list."""
        # current_node = self.head
        # node_count = 0
        # while current_node:
        #     node_count += 1
        #     current_node = current_node.find_next_node()
        # return node_count
        return self.size

    def insert_node(self, data):
        """Insert new node."""
        new_node = Node(data, self.head)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.size += 1
        # if self.head == None:
        #     self.head = new_node
        # else:
        #     new_node.next_node = self.head
        #     new_node.next_node.previous_node = new_node
        #     self.head = new_node

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

    def display(self, data):
        """Display the list."""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.find_next_node()

list_a = [1, 2, 3, 4]
# mylist = LinkedList()
# mylist.insert_node(5)
# mylist.insert_node(3)
# mylist.insert_node(98)

mylist = LinkedList()
mylist.display(list_a)
# for i in mylist:
#     print(i)

# list_a = (["1", "2", "3", "4"])
# l.insert_node(list_a, "a")
# l.insert_node(list_a, "b")
# l.insert_node(list_a, "c")
# print(l.display())

# l.remove_node(l.search('b'))
# print(l.display(list_a))
