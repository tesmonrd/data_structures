# -*- coding: utf8 -*-


def paren_check(text):
    """Check for correct parentheses."""
    while True:
        if text.find(")") < text.find("("):
            return(-1)
        elif text.rfind("(") > text.rfind(")"):
            return(1)
        elif text.find("(") < text.find(")"):
            return(0)
