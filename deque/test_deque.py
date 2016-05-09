# _*_ utf-8 _*_
"""Test Deque Data Structure."""
import pytest


APPEND_TEST = [([1, 2], 3, 3), (["heyhey", 23, 92, "datastructures", 0], 0, 0)]

POP_TEST = [([1, 2, 3, 4, 5], 5)]

PEEK_TEST = [([1, 2, 3, 4, 5], 4)]

SIZE_TEST = [([1, 2, 3, 4, 5, 6], 4)]


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


@pytest.mark.parametrize("list, result", POP_TEST)
def test_pop(list, result):
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    assert dq.pop() == result


@pytest.mark.parametrize("list, result", POP_TEST)
def test_pop_left(list, result):
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.appendleft(i)
    assert dq.popleft() == result


@pytest.mark.parametrize("list, result", PEEK_TEST)
def test_peek(list, result):
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    assert dq.peek() == result


@pytest.mark.parametrize("list, result", PEEK_TEST)
def test_peek_left(list, result):
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.appendleft(i)
    assert dq.peekleft() == result


@pytest.mark.parametrize("list, result", SIZE_TEST)
def test_size(list, result):
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    dq.pop()
    dq.pop()
    assert dq.size() == result


def test_pop_error():
    with pytest.raises(AttributeError):
        from deque import Deque
        dq = Deque()
        dq.append(1)
        dq.pop()
        assert dq.pop()


def test_pop_left_error():
    with pytest.raises(AttributeError):
        from deque import Deque
        dq = Deque()
        dq.appendleft(1)
        dq.popleft()
        assert dq.popleft()
