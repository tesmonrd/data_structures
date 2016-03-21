# _*_ utf=8 _*_


class BinHeap(object):
    """Implement a Binary-Heap."""

    def __init__(self):
        """Initialize the Binary-Heap."""
        self.heap = []
        self.size = 0

    def push(self, value):
        """Push new value into Binary-Heap and adjusts order."""
        self.heap.append(value)
        self.size += 1
        self._child_vs_parent(self.size - 1)
        print(self.heap)
        return self.heap

    def _child_vs_parent(self, i):
        """Compare the child to the parent."""
        while (i - 1) // 2 >= 0:
            if self.heap[(i - 1) // 2] < self.heap[i]:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2
        return self.heap[0]

    def pop(self):
        """Pop the root off of the Binary-Heap and adjusts order."""
        self._raise_to_top()
        self.heap = self._parent_vs_child(0)
        self.size -= 1
        return self.heap

    def _raise_to_top(self):
        """Raise the heap value upwards."""
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        return self.heap

    def _parent_vs_child(self, i):
        """Compare the parent to the child."""
        try:
            while (self.heap[i] < self.heap[2 * i] or
                    self.heap[i] < self.heap[2 * i + 1]):
                max_child = max(self.heap[2 * i], self.heap[2 * i + 1])
                if max_child > self.heap[i]:
                    new_head = self.heap.index(max_child)
                    self.heap[new_head], self.heap[i] = self.heap[i], self.heap[new_head]
                i = new_head
        except IndexError:
            pass
        return self.heap
