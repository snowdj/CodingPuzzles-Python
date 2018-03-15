def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    t = []
    for c in s:
        if len(t) == 0:
            t.append(c)
            continue
        if isPair(t[-1], c):
            del(t[-1])
        else:
            t.append(c)

    if len(t) > 0:
        return False
    return True

def isPair(c1, c2):
    if c1 is None or c2 is None:
        return False
    if (c1 == '[' and c2 == ']') or (c1 == '(' and c2 == ')') or c1 == '{' and c2 == '}':
        return True
    return False


if __name__ == "__main__":
    s = "{{)}"
    res = isValid(s)
    print(res)

