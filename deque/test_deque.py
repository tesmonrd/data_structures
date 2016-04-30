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


def test_pop_error():
    """Test pop an item from deque with nothing in it."""
    with pytest.raises(AttributeError):
        from deque import Deque
        dq = Deque()
        assert dq.pop()


def test_popleft_error():
    """Test popleft an item from deque with nothing in it."""
    with pytest.raises(AttributeError):
        from deque import Deque
        dq = Deque()
        assert dq.popleft()


@pytest.mark.parametrize("list, result", POP_TEST)
def test_pop(list, result):
    """Test pop of an item from deque."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    assert dq.pop() == result


@pytest.mark.parametrize("list, result", POP_TEST)
def test_pop_left(list, result):
    """Test popleft of an item from deque."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.appendleft(i)
    assert dq.popleft() == result


def test_peek_empty():
    """Test peek of an empty deque."""
    from deque import Deque
    dq = Deque()
    assert dq.peek() is None


def test_peek_solo():
    """Test peek of deque with one item."""
    from deque import Deque
    dq = Deque()
    dq.append(1)
    assert dq.peek() is None


@pytest.mark.parametrize("list, result", PEEK_TEST)
def test_peek(list, result):
    """Test peek for a list of multiple items."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    assert dq.peek() == result


def test_peek_left_empty():
    """Test peek of an empty deque."""
    from deque import Deque
    dq = Deque()
    assert dq.peekleft() is None


def test_peek_left_solo():
    """Test peek of deque with one item."""
    from deque import Deque
    dq = Deque()
    dq.append(1)
    assert dq.peekleft() is None


@pytest.mark.parametrize("list, result", PEEK_TEST)
def test_peek_left(list, result):
    """Test a peekleft of a deque with mutliple items."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.appendleft(i)
    assert dq.peekleft() == result


def test_size_empty():
    """Test that size is zero when the deque is empty."""
    from deque import Deque
    dq = Deque()
    assert dq.size() == 0


@pytest.mark.parametrize("list, result", SIZE_TEST)
def test_size(list, result):
    """Test the size of deque after popping a couple items off."""
    from deque import Deque
    dq = Deque()
    for i in list:
        dq.append(i)
    dq.pop()
    dq.pop()
    assert dq.size() == result
