# personal bin heap data structure
# import math

class BinHeap(object):
    """A."""

    def __init__(self):
        """A."""
        self.heap = [None]
        self.count = 0

    def push(self, value):
        """B."""
        self.heap.append(value)
        self.count += 1
        self._child_vs_parent(self.count)

    def _child_vs_parent(self, i):
        """C."""
        while i // 2 > 0:
            if self.heap[i // 2] < self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2

    def push 


# heap = [16, 9, 10, 8, 7, 4, 5]
bins = BinHeap()
bins.push(3)
bins.push(2)
bins.push(200)
