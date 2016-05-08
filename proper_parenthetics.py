# _*_ utf-8 _*_
"""Interview Challenge: Proper Parenthetics."""
from collections import Counter


def parens(string):
    """Check a string to make sure correct number of parenthesis are there."""
    paren_dict = Counter(string)
    if paren_dict[")"] < paren_dict["("]:
        return 1
    elif paren_dict[")"] > paren_dict["("]:
        return (-1)
    else:
        if all([paren_dict[")"] == paren_dict["("],
                string.find(")") > string.find("("),
                string.rfind(")") > string.rfind("(")]):
            return 0
        else:
            print(-1)
            return (-1)


def main():
    """Ask for a string input."""
    string = input(u'Input string here: \n')
    parens(string)

if __name__ == '__main__':
    main()
