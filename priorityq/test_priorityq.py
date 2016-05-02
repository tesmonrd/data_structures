# _*_ coding utf-8 _*_
"""Test Priority Queue."""
import pytest

LIST = [(35, "Mulla"), (92, False), (2, "Drizzy"), (93, "Rihanna"), (0, 62)]

LIST_2 = [(93, "Rihanna"),
          (92, False),
          (1000, "Bey"),
          (35, "Mulla"),
          (2, "Drizzy"),
          (0, 62)]

PUSH_TEST = [(LIST, (1000, "Bey"))]

CHECK_TEST = [(LIST_2, 5, (1000, "Bey"))]

POP_TEST = [(LIST_2, 93)]

RAISE_TEST = [(LIST_2, (2, "Drizzy"))]

PEEK_TEST = [(LIST_2, (1000, "Bey"))]

SWAP_TEST = [(LIST_2, 3)]

MC_TEST = [(LIST_2, (1000, "Bey"))]


@pytest.mark.parametrize("items, result", PUSH_TEST)
def test_insert(items, result):
    """Test the insert of the Priority Queue."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.insert((1000, "Bey")) == result


@pytest.mark.parametrize("items, size, result", CHECK_TEST)
def test_check(items, size, result):
    """Test that the check method returns the correct priority."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._check_priority((1000, "Bey"), size) == result


def test_pop_empty():
    """Test popping any empty priority queue."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


@pytest.mark.parametrize("items, result", POP_TEST)
def test_pop(items, result):
    """Test the pop method."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.pop() == result


@pytest.mark.parametrize("items, result", RAISE_TEST)
def test_raise_to_top(items, result):
    """Test that the last item is switched with the first item."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._raise_to_top() == result


@pytest.mark.parametrize("items, result", MC_TEST)
def test_max_child(items, result):
    """Test max_child."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._max_child(0) == result


@pytest.mark.parametrize("items, result", SWAP_TEST)
def test_swap(items, result):
    """Test swap."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._swap(1, 3) == result


@pytest.mark.parametrize("items, result", PEEK_TEST)
def test_peek(items, result):
    """Test peek."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.peek() == result
