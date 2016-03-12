def test_broken():
    """Test to see if there is a broken parenthesis."""
    from properparen import paren_check
    text = ")) help (("
    assert paren_check(text) == -1


def test_balanced():
    """Test to see if balanced."""
    from properparen import paren_check
    text = "()potato()"
    assert paren_check(text) == 0


def test_open():
    """Test to see if open."""
    from properparen import paren_check
    text = "())((it's friday))(("
    assert paren_check(text) == 1
