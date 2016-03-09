#  _*_ coding utf-8 _*_
import pytest


INSERT_TEST = [(10, 10), ("hey", "hey")]

LIST = [1, 2, 3, 4, 5]

SIZE_TEST = [(LIST, 5)]

REMOVE_TEST = [(LIST, 4)]


@pytest.mark.parametrize('value, result', INSERT_TEST)
def test_insert(value, result):
    """A."""
    from linked_list import LinkedList
    linked = LinkedList()
    assert linked.insert_node(value) == result


@pytest.mark.parametrize('value, result', SIZE_TEST)
def test_size(value, result):
    """B."""
    from linked_list import LinkedList
    linked = LinkedList()
    for i in LIST:
        linked.insert_node(i)
    assert linked.get_size() == result


@pytest.mark.parametrize('value, result', REMOVE_TEST)
def test_remove(value, result):
    """C."""
    from linked_list import LinkedList
    linked = LinkedList()
    for i in LIST:
        linked.insert_node(i)
    linked.remove_node(3)
    assert linked.get_size() == result
