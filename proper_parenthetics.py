# _*_ utf-8 _*_
"""Interview Challenge: Proper Parenthetics."""
# un-comment the line below to allow user input
# string = input(u'Input string here: \n')


def parens(string):
    """Check a string to make sure correct number of parenthesis are there."""
    count = 0
    for idx in string:
        if idx is u"(":
            count += 1
        elif idx is u")":
            count -= 1

    if count == 0:
        if (string.find(u")") > string.find(u"(")) and (string.rfind(u")") > string.rfind(u"(")):
            return 0
        else:
            return (-1)

    elif count < 0:
        return (-1)

    elif count > 0:
        return 1


if __name__ == '__main__':
    parens(string)
