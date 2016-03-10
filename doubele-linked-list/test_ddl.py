# _*_ coding utf-8 _*_
import pytest


INSERT_TEST = [("hey", "hey"), (5, 5)]

APPEND_TEST = [("YOLO", "YOLO"), (5678, 5678)]

POP_TEST = [(5, 5)]

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

@pytest.mark.parametrize("data, result", POP_TEST)
def test_pop(data, result):
    """Test to see if the append function works properly."""
    from ddl import DoubleLink
    dl = DoubleLink()
    assert dl.pop(data) == result
