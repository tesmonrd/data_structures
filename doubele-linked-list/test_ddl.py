# _*_ coding utf-8 _*_
import pytest


INSERT_TEST = [("hey", "hey"), (5, 5)]

APPEND_TEST = [("YOLO", "YOLO"), (5678, 5678)]


@pytest.mark.parametrize("data, result", INSERT_TEST)
def test_insert(data, result):
    """Test to see if the insert function works properly."""
    from ddl import DoubleLink
    dl = DoubleLink()
    assert dl.insert(data) == result


@pytest.mark.parametrize("data, result", APPEND_TEST)
def test_append(data, result):
    """Test to see if the append function works properly."""
    from ddl import DoubleLink
    dl = DoubleLink()
    assert dl.append(data) == result


def test_shift():
    """Test to see if shift works, returns shift value."""
    from ddl import DoubleLink
    dl = DoubleLink()
    dl.insert(2)
    dl.append(3)
    dl.append(4)
    dl.append(5)
    assert dl.shift() == 5


def test_pop():
    """Test to see if pop works, returns popped value."""
    from ddl import DoubleLink
    dl = DoubleLink()
    dl.insert(2)
    dl.insert(3)
    dl.append(4)
    dl.append(5)
    assert dl.pop() == 3
