# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return s

        slist = s.split()
        return " ".join(slist[::-1])

class Solution1(object):
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])