import pytest



PUSH_TEST = [("4", "4")]

@pytest.mark.parametrize('value, result', PUSH_TEST)
def test_push(value, result):
    from stack import Stack
    push = Stack()
    assert push.push(value) == result
