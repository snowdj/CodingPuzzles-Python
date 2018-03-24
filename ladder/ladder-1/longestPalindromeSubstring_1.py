def longestPalindrome(s):
    # write your code here
    if s is None or len(s) <= 1:
        return s

    sl = list(s)  # convert any iterable to a list

    maxlen = 0
    start_pos = -1
    for i in range(1, len(sl)):
        tlen = 0
        if sl[i] == sl[i - 1]:
            tlen, tpos = findLongestPalindrome(sl, i - 1, i)
            if tlen > maxlen:
                maxlen = tlen
                start_pos = tpos
        if i < len(sl) - 1 and sl[i - 1] == sl[i + 1]:
            tlen, tpos = findLongestPalindrome(sl, i - 1, i + 1)
            if tlen > maxlen:
                maxlen = tlen
                start_pos = tpos
        else:
            continue

    if start_pos == -1:
        return ""
    return s[start_pos:start_pos + maxlen]

def findLongestPalindrome(s, pos_left, pos_right):
    if pos_left is None or pos_right is None:
        return 0, -1

    dist = pos_right - pos_left + 1
    while (pos_left - 1 >= 0 and pos_right + 1 <= len(s) - 1):
        if s[pos_left-1] == s[pos_right+1]:
            dist += 2
            pos_left -= 1
            pos_right += 1
        else:
            break

    return dist, pos_left


def findLongestPalindrome_ref(s, pos_left, pos_right):
    pass

if __name__ == "__main__":
    test_str = "aaaa"
    expected_result = "aaaa"
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "a"
    expected_result = "a"
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "abccccdd"
    expected_result = "cccc"
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "abccb"
    expected_result = "bccb"
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)