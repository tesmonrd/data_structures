# _*_ utf-8 _*_
"""Test Proper Parenthetics."""
import pytest

PARAMS_TEST = [("There ( (are more ( open ( parentheses then closed", 1),
               ("(The proper amount of () are in (this) comment)", 0),
               ("This comment starts with a ))(( closing parentheses", (-1)),
               ("(((", 1),
               (")))", (-1)),
               (")(()", (-1)),
               ("()", 0),
               ]


@pytest.mark.parametrize("string, result", PARAMS_TEST)
def test_params(string, result):
    """Test to make sure that the correct int is return if string is broken."""
    from proper_parenthetics import parens
    assert parens(string) == result
