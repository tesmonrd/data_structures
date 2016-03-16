# personal bin heap data structure
# import math


class BinHeap(object):
    """A."""

    def __init__(self):
        """A."""
        self.heap = [None, 16, 9, 10, 8, 7, 4, 5]
        self.count = 7

    def push(self, value):
        """B."""
        print(self.heap)
        self.heap.append(value)
        self.count += 1
        self._child_vs_parent(self.count)
        print(self.heap)
        return self.heap

    def _child_vs_parent(self, i):
        """C."""
        while i // 2 > 0:
            if self.heap[i // 2] < self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2
        return self.heap[i]

    def _parent_vs_child(self, i):
        while i < (2 * i) and i < (2 * i + 1):
            max_child = max(2 * i, 2 * i + 1)
            index1 = max_child / 2
            index2 = max_child / 2 - 1
            if max_child == 2 * i:
                self.heap[int(index1)], self.heap[i] = self.heap[i], self.heap[int(index1)]
                i = int(index1)
            else:
                self.heap[int(index2)], self.heap[i] = self.heap[i], self.heap[int(index2)]
                i = int(index2)
        return self.heap[i]

    def _raise_to_top(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        print("OLD TOP: " + str(self.heap[1]))
        print("NEW TOP: " + str(self.heap[-1]))
        self.heap.pop()
        print("***************")
        print(self.heap)
        return self.heap[1]

    def pop(self):
        """A."""
        self._raise_to_top()
        print(self.heap[1])
        self._parent_vs_child(1)
        print(self.heap)
        # if self.heap[-1] > self.heap[1]:

# heap = [16, 9, 10, 8, 7, 4, 5]
bins = BinHeap()
# print(self.heap)
bins.push(200)
# print(self.heap)
bins.pop()
bins.pop()
bins.pop()
