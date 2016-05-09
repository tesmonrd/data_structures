#  _*_ coding utf-8 _*_
"""Test linked list functions."""
import pytest

INSERT_TEST = [(10, 10), (u"Test", u"Test")]

LIST = [1, 2, 3, 4, 5]

SIZE_TEST = [(LIST, 5)]

POP_TEST = [(2)]

SEARCH_TEST_ERROR = [(33, 3)]

SEARCH_TEST = [(3, 3)]

REMOVE_TEST = [(3, 3)]

# *************************************************************


@pytest.mark.parametrize('value, result', INSERT_TEST)
def test_insert(value, result):
    """Testing to make sure the correct thing is inserted."""
    from linked import LinkedList
    ll = LinkedList()
    assert ll.insert(value) == result


@pytest.mark.parametrize('value, result', SIZE_TEST)
def test_size(value, result):
    """Testing to check size."""
    from linked import LinkedList
    ll = LinkedList()
    for i in LIST:
        ll.insert(i)
    assert ll.size() == result


@pytest.mark.parametrize('result', POP_TEST)
def test_pop(result):
    """Testing to see if the last element is popped and the head has moved."""
    """I will insert 4 items to the linked-list then pop it twice.
       Then run the test and see if the value matches"""
    from linked import LinkedList
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.pop()
    ll.pop()
    assert ll.pop() == result


@pytest.mark.parametrize('value, result', SEARCH_TEST_ERROR)
def test_search_error(value, result):
    """Test to is that an error is caught if the wrong item is searched."""
    from linked import LinkedList
    with pytest.raises(ValueError):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)
        ll.insert(5)
        ll.insert(6)
        assert ll.search(value) == result


@pytest.mark.parametrize('value, result', SEARCH_TEST)
def test_search(value, result):
    """Testing to search for the 3 element in a linked-list of 6 items."""
    from linked import LinkedList
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    assert ll.search(value) == result


@pytest.mark.parametrize('value, result', REMOVE_TEST)
def test_remove(value, result):
    """Check to make sure that the item is removed and return value."""
    from linked import LinkedList
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    assert ll.remove(value) == result
