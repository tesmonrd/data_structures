#  _*_ coding utf-8 _*_
"""Implement a Linked List."""


class Node(object):
    """Node establishes functions that move within the list."""

    def __init__(self, val=None, next_node=None):
        """Initialize the list."""
        self.val = val
        self.next_node = next_node


class LinkedList(object):
    """Linked List Implementation."""

    def __init__(self, lst=[]):
        """Initialize the head of the node to (None is not given)."""
        self.head = None
        self.length = 0
        for val in lst:
            self.insert(val)

    def insert(self, val):
        """Insert new node to Linked List."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1
        return new_node.val

    def pop(self):
        """Pop the head and return its value."""
        try:
            old_head = self.head
            self.head = self.head.next_node
            self.length -= 1
            return old_head.val
        except AttributeError:
            return None

    def size(self):
        """Get the total count of nodes in list."""
        return self.length

    def search(self, val):
        """Search for a specific node in list, if not present return None."""
        try:
            current_node = self.head
            while True:
                if current_node.val == val:
                    return current_node
                current_node = current_node.next_node
        except AttributeError:
            return None

    def remove(self, node):
        """Remove a specific node in the Linked List."""
        if self.size() > 1:
            current_node = self.head
            previous_node = None
            while True:
                if current_node == node:
                    self.length -= 1
                    break
                previous_node = current_node
                current_node = current_node.next_node
            previous_node.next_node = current_node.next_node
            current_node = previous_node
        else:
            self.head = None

    def display(self):
        """Display the Linked List as a tuple."""
        node_list = []
        node = self.head
        if node is not None:
            while node.next_node is not None:
                node_list.append(node.val)
                node = node.next_node
            node_list.append(node.val)
        print(tuple(node_list))
        return(tuple(node_list))  # Simply for testing purposes


# if __name__ == '__main__':
#     # ll = LinkedList()
#     ll = LinkedList([10, 20, 30, 40])
#     ll.display()
#     # ll.insert(10)
#     # ll.insert(20)
#     # ll.insert(30)
#     # ll.insert(40)
#     # print("SIZE: " + str(ll.size()))
#     # node = ll.head
#     # while node is not None:
#     #     print(node.val)
#     #     node = node.next_node
#     # print("***************")
#     # ll.pop()
#     # print(ll.search(40))
#     # ll.remove(ll.search(30))
#     # node = ll.head
#     # while node is not None:
#     #     print(node.val)
#     #     node = node.next_node
#     # ll.remove(ll.search(10))
#     # node = ll.head
#     # while node is not None:
#     #     print(node.val)
#     #     node = node.next_node
