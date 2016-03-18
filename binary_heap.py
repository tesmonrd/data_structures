# personal bin heap data structure


class BinHeap(object):
    """A."""

    def __init__(self):
        """A."""
        self.heap = []
        self.size = 0

    # def hey(self):
    #     print(self.heap)
    #     return self.heap

    def push(self, value):
        """B."""
        self.heap.append(value)
        self.size += 1
        self._child_vs_parent(self.size - 1)
        print(self.heap)
        return self.heap

    def _child_vs_parent(self, i):
        """C."""
        while (i - 1) // 2 >= 0:
            if self.heap[(i - 1) // 2] < self.heap[i]:
                self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2
        return self.heap[0]

    def pop(self):
        """A."""
        self._raise_to_top()
        self.heap = self._parent_vs_child(0)
        self.size -= 1
        return self.heap

    def _raise_to_top(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        return self.heap

    def _parent_vs_child(self, i):
        try:
            while self.heap[i] < self.heap[2 * i] or self.heap[i] < self.heap[2 * i + 1]:
                max_child = max(self.heap[2 * i], self.heap[2 * i + 1])
                if max_child > self.heap[i]:
                    new_head = self.heap.index(max_child)
                    self.heap[new_head], self.heap[i] = self.heap[i], self.heap[new_head]
                i = new_head
        except IndexError:
            pass
        return self.heap

bins = BinHeap()
bins.push(200)
bins.push(30)
bins.push(40)
bins.push(50)
bins.push(1)
bins.push(20)
bins.hey()
bins.pop()
bins.hey()
bins.push(400)
bins.pop()
bins.hey()
