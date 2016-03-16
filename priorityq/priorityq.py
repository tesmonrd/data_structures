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
        print()
        while (i - 1) // 2 >= 0:
            if self.heap[(i - 1) // 2][0] < self.heap[i][0]:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2
        return self.heap


p = PQ()
p.insert((1, 2))
p.insert((2, 2))
p.insert((3, 2))
p.insert((5, 2))
