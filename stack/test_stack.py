"""Testing the Stack data-structure."""
import pytest

PUSH_TEST = [("4", "4")]

count_list = [1, 2, 3, 99, "potato"]

POP_TEST = [(count_list, 4)]

COUNT_TEST = [(count_list, 5)]


@pytest.mark.parametrize('value, result', PUSH_TEST)
def test_push(value, result):
    """Test to see if given value is pushed to stack."""
    from stack import Stack
    push = Stack()
    assert push.push(value) == result


@pytest.mark.parametrize('count_list, count', COUNT_TEST)
def test_count(count_list, count):
    """Test to see if stack count is correct."""
    from stack import Stack
    s = Stack()
    for i in count_list:
        s.push(i)
    assert s.size() == count


@pytest.mark.parametrize('count_list, result', POP_TEST)
def test_pop(count_list, result):
    """Test to see if last value in stack is popped out."""
    from stack import Stack
    s = Stack()
    for i in count_list:
        s.push(i)
    s.pop()
    assert s.size() == 4
