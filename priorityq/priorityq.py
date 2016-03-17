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

    def pop(self):
        """A."""
        self.heap = self._raise_to_top()
        self._reshuffle()
        self.size -= 1
        return self.heap

    def _raise_to_top(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        self.heap.pop()
        return self.heap

    def _reshuffle():
    #   while self.heap[i] < self.heap[2 * i] or self.heap[i] < self.heap[2 * i + 1]:
            while self.heap[i] < 
        pass


    # def _parent_vs_child(self, i):
    #     try:
    #             max_child = max(self.heap[2 * i], self.heap[2 * i + 1])
    #             if max_child > self.heap[i]:
    #                 new_head = self.heap.index(max_child)
    #                 self.heap[new_head], self.heap[i] = self.heap[i], self.heap[new_head]
    #             i = new_head
    #     except IndexError:
    #         pass
    #     # if 
    #     return self.heap



p = PQ()
p.insert((1, 2))
p.insert((2, 2))
p.insert((3, 2))
p.insert((5, 2))
