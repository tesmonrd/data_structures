# _*_ utf-8 _*_
"""Test Deque Data Structure."""
import pytest


APPEND_TEST = [([1, 2], 3, 3), (["heyhey", 23, 92, "datastructures", 0], 0, 0)]


@pytest.mark.parametrize("list, val, result", APPEND_TEST)
def test_append(list, val, result):
    """Test to see that a node is appended to the tail."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    assert dq.append(val) == result


@pytest.mark.parametrize("list, val, result", APPEND_TEST)
def test_appendleft(list, val, result):
    """Test to see that a node is appended to the head."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.appendleft(i)
    assert dq.appendleft(val) == result
