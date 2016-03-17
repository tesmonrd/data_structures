# -*- coding:utf-8 -*-


class PQ(object):
    """C."""

    def __init__(self):
        """A."""
        self.heap = []
        self.size = 0

    def insert(self, item):
        """B."""
        self.heap.append(item)
        self.size += 1
        self._check_priority(item, self.size - 1)
        print(self.heap)

    def _check_priority(self, tup, i):
        """A."""
        while (i - 1) // 2 >= 0:
            if self.heap[(i - 1) // 2][0] < self.heap[i][0]:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2
        return self.heap

    def pop(self):
        """A."""
        self._raise_to_top()
        self.heap = self._max_child(0)
        self.size -= 1
        return self.heap

    def _raise_to_top(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        popped = self.heap.pop()
        return self.heap

    def _max_child(self, i):
        try:
            while self.heap[i] <= self.heap[2 * i + 1] or self.heap[i] <= self.heap[2 * i + 2]:
                high_child = max(self.heap[2 * i + 1], self.heap[2 * i + 2])
                i = self._swap(i, self.heap.index(high_child))
        except IndexError:
            pass
        return self.heap

    def _swap(self, parent_i, child_i,):
        self.heap[child_i], self.heap[parent_i] = self.heap[parent_i], self.heap[child_i]
        new_child = self.heap[child_i]
        return self.heap.index(new_child)
