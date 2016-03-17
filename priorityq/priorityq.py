# -*- coding:utf-8 -*-
"""Priority Queue Data Structure."""


class PriorityQueue(object):
    """Priority Queue Class."""

    def __init__(self):
        """Instantiate the priority queue data structure."""
        self.heap = []
        self.size = 0
    # @property
    # def _size(self):
    #     return self._size

    def insert(self, item):
        """Insert an item into the queue."""
        self.heap.append(item)
        self.size += 1
        self._check_priority(item, self.size - 1)
        print(self.heap)
        return self.heap[0]

    def _check_priority(self, tup, i):
        """Check that the parent is larger, if not swap places with child."""
        while (i - 1) // 2 >= 0:
            if self.heap[(i - 1) // 2][0] < self.heap[i][0]:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2
        print("CHECK: " + str(self.heap[0]))
        return self.heap[0]

    def pop(self):
        """Remove the most important item from the queue.."""
        self._raise_to_top()
        self.heap = self._max_child(0)
        self.size -= 1
        return self.heap[0]

    def _raise_to_top(self):
        """Switch the bottom and top item to remove the most important one."""
        # Requires O(1) to remove from end of list and O(n) from the beginning
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        print("POP: " + str(self.heap[-1]))
        self.heap.pop()
        return self.heap[-1]

    def _max_child(self, i):
        """If a child is more important then its parent, swap them."""
        try:
            while self.heap[i] <= self.heap[2 * i + 1] or self.heap[i] <= self.heap[2 * i + 2]:
                high_child = max(self.heap[2 * i + 1], self.heap[2 * i + 2])
                i = self._swap(i, self.heap.index(high_child))
        except IndexError:
            pass
        return self.heap[0]

    def _swap(self, parent_i, child_i,):
        """Swap the child and parent in list."""
        self.heap[child_i], self.heap[parent_i] = self.heap[parent_i], self.heap[child_i]
        new_child = self.heap[child_i]
        return self.heap.index(new_child)

    def peek(self):
        """Return the most important item in queue."""
        return self.heap[0]
