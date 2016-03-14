# _*_ utf-8 _*_
"""Test Proper Parenthetics."""
import pytest

PARAMS_TEST = [(u"(The proper amount of () are in (this) comment)", 0),
               (u"This comment starts with a ))(( closing parentheses", (-1)),
               (u"(There are more ( open ( parentheses then closed))", 1)
               ]


@pytest.mark.parametrize("strings, result", PARAMS_TEST)
def test_params(strings, result):
    """Test to make sure that the correct int is return is string is broken."""
    from proper_parenthetics import parens
    assert parens(strings) == result
