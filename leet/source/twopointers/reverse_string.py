class Solution:
    def reverseString(s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) <= 1:
            return s

        i = 0
        j = len(s) - 1
        sa = list(s)
        while (i < j):
            tmp = sa[i]
            sa[i] = sa[j]
            sa[j] = tmp
            i += 1
            j -= 1

        return ''.join(sa)


if __name__ == "__main__":
    sln = Solution()

    test_s = "hello"
    res = sln.reverseString(test_s)
    print(res)