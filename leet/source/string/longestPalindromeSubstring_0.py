def longestPalindrome(s):
    # write your code here
    if s is None or len(s) <= 1:
        return 0

    sl = list(s)  # convert any iterable to a list

    maxlen = 0
    for i in range(1, len(sl)):
        tlen = 0
        if sl[i] == sl[i - 1]:
            tlen = findLongestPalindrome(sl, i - 1, i)
            if tlen > maxlen:
                maxlen = tlen
        if i < len(sl) - 1 and sl[i - 1] == sl[i + 1]:
            tlen = findLongestPalindrome(sl, i - 1, i + 1)
            if tlen > maxlen:
                maxlen = tlen
        else:
            continue

    return maxlen


def findLongestPalindrome(s, pos_left, pos_right):
    if pos_left is None or pos_right is None:
        return 0

    dist = pos_right - pos_left + 1
    while (pos_left > 0 and pos_right < len(s) - 1):
        if pos_left - 1 >= 0 and pos_right + 1 <= len(s) - 1 and s[pos_left - 1] == s[pos_right + 1]:
            dist += 2
            pos_left -= 1
            pos_right += 1
        else:
            break

    return dist


if __name__ == "__main__":
    test_str = "abccccdd"
    expected_result = 4
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert(res == expected_result)

    test_str = "abccb"
    expected_result = 4
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)
