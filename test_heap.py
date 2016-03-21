# _*_ coding=utf-8 _*_

HEAP_LIST = [39, 67, 23, 1, 765, 3, 2, 87]


def test_push():
    from binary_heap import BinHeap
    bins = BinHeap()
    for i in HEAP_LIST:
        bins.push(i)
    assert bins.heap[0] == 765


def test_pop():
    from binary_heap import BinHeap
    bins = BinHeap()
    for i in HEAP_LIST:
        bins.push(i)
    bins.pop()
    assert bins.heap[0] == 87
