class Solution():
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None

        if len(s) <= 1:
            return s

        list_s = list(s)

        maxlen = 1
        result = list_s[0]
        for i in range(1, len(list_s)):
            i_maxlen = 0
            i_start = 0
            if list_s[i-1] == list_s[i]:
                i_maxlen, i_start = self.search(list_s, i-1, i)
                if i_maxlen > maxlen:
                    maxlen = i_maxlen
                    result = s[i_start:i_start+i_maxlen]
                if maxlen == len(s):
                    return result
            if i + 1 < len(list_s) and list_s[i-1] == list_s[i+1]:
                i_maxlen, i_start = self.search(list_s, i-1, i+1)
                if i_maxlen > maxlen:
                    maxlen = i_maxlen
                    result = s[i_start:i_start+i_maxlen]
                if maxlen == len(s):
                    return result

        return result

    def search(self, source, left, right):
        maxlen = right - left + 1
        start = left

        nleft = left - 1
        nright = right + 1
        while nleft >= 0 and nright <= len(source) - 1:
            if source[nleft] == source[nright]:
                maxlen += 2
                start = nleft
            else:
                break
            nleft -= 1
            nright += 1

        return maxlen, start

if __name__ == "__main__":
    sln = Solution()
    test_str = "aaaa"
    expected_result = "aaaa"
    res = sln.longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "a"
    expected_result = "a"
    res = sln.longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "abccccdd"
    expected_result = "cccc"
    res = sln.longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "abccb"
    expected_result = "bccb"
    res = sln.longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "babadada"
    expected_result = "adada"
    res = sln.longestPalindrome(test_str)
    print("test_str: {0}")