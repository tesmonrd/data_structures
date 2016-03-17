# _*_ coding utf-8 _*_
"""Test Priority Queue."""
import pytest

LIST = [(35, "Mulla"), (92, False), (2, "Drizzy"), (93, "Rihanna"), (0, 62)]

END_LIST = [(1000, "Bey"), (93, "Rihanna"), (92, False), (35, "Mulla"), (2, "Drizzy"), (0, 62)]

PUSH_TEST = [(LIST, (1000, "Bey"))]


@pytest.mark.parametrize("items, result", PUSH_TEST)
def test_push(items, result):
    """A."""
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    for idx in items:
        pq.insert(idx)
    assert pq.insert((1000, "Bey")) == result

