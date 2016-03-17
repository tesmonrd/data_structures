# _*_ coding utf-8 _*_
"""Test Priority Queue."""
import pytest

LIST = [(35, "Mulla"), (92, False), (2, "Drizzy"), (93, "Rihanna"), (0, 62)]

LIST_2 = [(93, "Rihanna"), (92, False), (1000, "Bey"), (35, "Mulla"), (2, "Drizzy"), (0, 62)]

# FINAL_LIST = [(1000, "Bey")]

PUSH_TEST = [(LIST, (1000, "Bey"))]

CHECK_TEST = [(LIST_2, 5, (1000, "Bey"))]

POP_TEST = [(LIST_2, (93, "Rihanna"))]

RAISE_TEST = [(LIST_2, (2, "Drizzy"))]

# MAX_ITEM = [(LIST_2,)]


@pytest.mark.parametrize("items, result", PUSH_TEST)
def test_push(items, result):
    """A."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.insert((1000, "Bey")) == result


@pytest.mark.parametrize("items, size, result", CHECK_TEST)
def test_check(items, size, result):
    """A."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._check_priority((1000, "Bey"), size) == result


@pytest.mark.parametrize("items, result", POP_TEST)
def test_pop(items, result):
    """A."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.pop() == result


@pytest.mark.parametrize("items, result", RAISE_TEST)
def test_raise_to_top(items, result):
    """A."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq._raise_to_top() == result


# @pytest.mark.parametrize(", ", )
