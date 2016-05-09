"""Test Linked List functions."""
import pytest

INSERT_TEST = [(10, 10), (u"Test", u"Test")]

LIST = [1, 2, 3, 4, 5]

SIZE_TEST = [(LIST, 5), ([20, "hey"], 2), ([x for x in range(0, 100)], 100)]

POP_TEST = [([2, "get", 354, False], False), ([True, "nope", 24], 24)]

SEARCH_TEST_ERROR = [([44, 22, 66], 33, None),
                     ([77, True, 55, 99, 11], False, None)]

SEARCH_TEST = [([22, 77, 55, True, "eyy"], "eyy", "eyy"),
               ([44, 88, False, "nope", 11], False, False)]

REMOVE_TEST = [([4, 2, 6, 3, 5], 3, (5, 6, 2, 4)),
               ([True, 23, "Munir", False], True, (False, "Munir", 23)),
               ([1, 2], 1, (2,)),
               ([1], 1, ())]

# *************************************************************


def test_initialized_list():
    """Test that you can initialize with a list of values."""
    from linked_list import LinkedList
    ll = LinkedList([1, 2, 3, 4, 5])
    assert ll.display() == (5, 4, 3, 2, 1)


@pytest.mark.parametrize('value, result', INSERT_TEST)
def test_insert(value, result):
    """Testing to make sure the correct thing is inserted."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.insert(value) == result


def test_empty_lst():
    """Test size of list with no nodes."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.size() == 0


@pytest.mark.parametrize('value, result', SIZE_TEST)
def test_size(value, result):
    """Test to check size."""
    from linked_list import LinkedList
    ll = LinkedList()
    for val in value:
        ll.insert(val)
    assert ll.size() == result


def test_pop_empty():
    """Test popping a list of no nodes."""
    from linked_list import LinkedList
    ll = LinkedList()
    assert ll.pop() is None


@pytest.mark.parametrize('lst, result', POP_TEST)
def test_pop(lst, result):
    """Test the pop function to see that it returns the head node."""
    from linked_list import LinkedList
    ll = LinkedList()
    for val in lst:
        ll.insert(val)
    assert ll.pop() == result


@pytest.mark.parametrize('lst, value, result', SEARCH_TEST_ERROR)
def test_search_error(lst, value, result):
    """Test to is that an error is caught if the wrong item is searched."""
    from linked_list import LinkedList
    ll = LinkedList()
    for val in lst:
        ll.insert(val)
    assert ll.search(value) is result


@pytest.mark.parametrize('lst ,value, result', SEARCH_TEST)
def test_search(lst, value, result):
    """Test the search for the node using the ."""
    from linked_list import LinkedList
    ll = LinkedList()
    for val in lst:
        ll.insert(val)
    assert ll.search(value).val == result


@pytest.mark.parametrize('lst, value, result', REMOVE_TEST)
def test_remove(lst, value, result):
    """Check to make sure that the item is removed and return value."""
    from linked_list import LinkedList
    ll = LinkedList()
    for val in lst:
        ll.insert(val)
    node = ll.search(value)
    ll.remove(node)
    assert ll.display() == result
