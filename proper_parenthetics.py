# _*_ utf-8 _*_
"""Interview Challenge: Proper Parenthetics."""


def parens(string):
    """Check a string to make sure correct number of parenthesis are there."""
    count = 0
    for idx in string:
        if idx is u"(":
            count += 1
        elif idx is u")":
            count -= 1

    if count > 0:
        print(1)
        return 1

    elif count < 0:
        print(-1)
        return (-1)

    else:
        if (string.find(u")") > string.find(u"(")) and (string.rfind(u")") > string.rfind(u"(")):
            print(0)
            return 0
        else:
            print(-1)
            return (-1)


# un-comment the lines below to allow user input on command line
if __name__ == '__main__':
    string = input(u'Input string here: \n')
    parens(string)