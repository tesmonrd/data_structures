#  _*_ coding utf-8 _*_
"""Test queue functions."""
import pytest

# *************************************************************


@pytest.mark.parametrize()
def test_enqueue():
    """Test to see that items are add to queue."""
    from queue_2 import Queue
    q = Queue()
    assert 1 == 1
