# _*_ coding utf-8 _*_
"""Test Priority Queue."""
import pytest

LIST = [(35, "Mulla"), (92, False), (2, "Drizzy"), (93, "Rihanna"), (0, 62)]

LIST_2 = [(93, "Rihanna"), (92, False), (1000, "Bey"), (35, "Mulla"), (2, "Drizzy"), (0, 62)]

PUSH_TEST = [(LIST, (1000, "Bey"))]

CHECK_TEST = [(LIST_2, 5, (1000, "Bey"))]

POP_TEST = [(LIST_2, 93)]

RAISE_TEST = [(LIST_2, (2, "Drizzy"))]

PEEK_TEST = [(LIST_2, (1000, "Bey"))]

SWAP_TEST = [(LIST_2, 3)]

MC_TEST = [(LIST_2, (1000, "Bey"))]


@pytest.mark.parametrize("items, result", PUSH_TEST)
def test_push(items, result):
    """Test Push."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.insert((1000, "Bey")) == result


@pytest.mark.parametrize("items, size, result", CHECK_TEST)
def test_check(items, size, result):
    """Test Check."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._check_priority((1000, "Bey"), size) == result


@pytest.mark.parametrize("items, result", POP_TEST)
def test_pop(items, result):
    """Test Pop."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.pop() == result


@pytest.mark.parametrize("items, result", RAISE_TEST)
def test_raise_to_top(items, result):
    """Test raise_to_top."""
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
