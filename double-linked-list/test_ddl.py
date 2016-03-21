# _*_ coding utf-8 _*_
"""Test of DoubleLinkList."""
import pytest

LIST = [1, 2, 3, 4, 5]

LIST2 = ["python", "1", 100, "hdjdnd", 9090, "401"]

INSERT_TEST = [("hey", "hey"), (5, 5)]

APPEND_TEST = [("YOLO", "YOLO"), (5678, 5678)]

POP_TEST = [(LIST, 5), (LIST2, "401")]

SHIFT_TEST = [(LIST, 1), (LIST2, "python")]


@pytest.mark.parametrize("data, result", INSERT_TEST)
def test_insert(data, result):
    """Test to see if the insert function works properly."""
    from double_linked import DoubleLink
    dl = DoubleLink()
    assert dl.insert(data) == result


@pytest.mark.parametrize("data, result", APPEND_TEST)
def test_append(data, result):
    """Test to see if the append function works properly."""
    from double_linked import DoubleLink
    dl = DoubleLink()
    assert dl.append(data) == result


@pytest.mark.parametrize("val, result", POP_TEST)
def test_pop(val, result):
    """Test to see if the pop function works properly."""
    from double_linked import DoubleLink
    dl = DoubleLink()
    for i in val:
        dl.insert(i)
    assert dl.pop() == result


@pytest.mark.parametrize("val, result", SHIFT_TEST)
def test_shift(val, result):
    """Test to see if the pop function works properly."""
    from double_linked import DoubleLink
    dl = DoubleLink()
    for i in val:
        dl.insert(i)
    assert dl.shift() == result
