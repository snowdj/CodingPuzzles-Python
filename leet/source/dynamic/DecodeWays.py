def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if s is None or s == '':
        return 0

    if len(s) == 1:
        if s == '0':
            return 0
        return 1

    ways = [0 for k in range(len(s))]
    if (int(s[0]) > 0):
        ways[0] = 1
    else:
        return 0

    if s[1] == '0':
        if (int(s[0:2]) > 0 and int(s[0:2]) <= 26):
            ways[1] = ways[0]
        else:
            return 0
    else:
        if (int(s[0:2]) > 0 and int(s[0:2]) <= 26):
            ways[1] = ways[0] + 1
        else:
            ways[1] = ways[0]

    for i in range(2, len(s)):
        if s[i] == '0':
            if int(s[i - 1]) > 0 and int(s[i - 1:i + 1]) >= 1 and int(s[i - 1:i + 1]) <= 26:
                ways[i] = ways[i-2]
            else:
                return 0
        else:
            if int(s[i - 1]) > 0 and int(s[i - 1:i + 1]) >= 1 and int(s[i - 1:i + 1]) <= 26:
                ways[i] = ways[i-2] + ways[i-1]
            else:
                ways[i] = ways[i-1]

    return ways[-1]

if __name__ == "__main__":
    test_s = "1212"
    res = numDecodings(test_s)
    print(res)

    test_s = "10"
    res = numDecodings(test_s)
    print(res)

    test_s = "01"
    res = numDecodings(test_s)
    print(res)

    test_s = "110"
    res = numDecodings(test_s)
    print(res)
