# personal bin heap test

import pytest

HEAP_LIST = [39, 67, 23, 1, 765, 3, 2, 87]


def test_push():
    from bins import BinHeap
    bins = BinHeap()
    for i in HEAP_LIST:
        bins.push(i)
    assert bins.heap[1] == 765
