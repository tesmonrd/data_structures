#  _*_ coding utf-8 _*_
"""Test queue functions."""
import pytest

LIST_TEST = [1, 2, 3, 4, 5]

LIST_TEST2 = [1, "hey", "yoyo", 25, True, 32, 99]

SIZE_TEST = [(LIST_TEST, 5), (LIST_TEST2, 7)]

ENQUEUE_TEST = [(4, 4), ("YOLO", "YOLO")]

DEQUEUE_TEST = [(LIST_TEST, 4)]

PEEK_TEST = [(LIST_TEST, 4)]

PEEK_TEST_ERROR = [(None)]


# *************************************************************


@pytest.mark.parametrize('value, result', ENQUEUE_TEST)
def test_enqueue(value, result):
    """Test to see that values are add to queue."""
    from queue import Queue
    q = Queue()
    assert q.enqueue(value) == result


@pytest.mark.parametrize("value, result", SIZE_TEST)
def test_size(value, result):
    """Test see that size of the queue is correct."""
    from queue import Queue
    q = Queue()
    for i in value:
        q.enqueue(i)
    assert q.size() == result


@pytest.mark.parametrize("value, result", DEQUEUE_TEST)
def test_dequeue(value, result):
    """Test to see that the correct value is removed from queue."""
    from queue import Queue
    q = Queue()
    for i in value:
        q.enqueue(i)
    q.dequeue()
    assert q.dequeue() == result


@pytest.mark.parametrize("value, result", PEEK_TEST)
def test_peek(value, result):
    """Test to see if we can peek at the next value in queue."""
    from queue import Queue
    q = Queue()
    for i in value:
        q.enqueue(i)
    assert q.peek() == result
