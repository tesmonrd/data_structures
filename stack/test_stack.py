import pytest


PUSH_TEST = [("4", "4")]

COUNT_LIST = [1, 2, 3, 99, "potato"]

POP_TEST = [(COUNT_LIST, 4)]

COUNT_TEST = [(COUNT_LIST, 5)]


@pytest.mark.parametrize('value, result', PUSH_TEST)
def test_push(value, result):
    """Test to see if given value is pushed to stack."""
    from stack import Stack
    push = Stack()
    assert push.push(value) == result


@pytest.mark.parametrize('COUNT_LIST, count', COUNT_TEST)
def test_count(COUNT_LIST, count):
    """Test to see if stack count is correct."""
    from stack import Stack
    s = Stack()
    for i in COUNT_LIST:
        s.push(i)
    assert s.size() == count


@pytest.mark.parametrize('COUNT_LIST, result', POP_TEST)
def test_pop(COUNT_LIST, result):
    """Test to see if last value in stack is popped out."""
    from stack import Stack
    s = Stack()
    for i in COUNT_LIST:
        s.push(i)
    s.pop()
    assert s.size() == 4
