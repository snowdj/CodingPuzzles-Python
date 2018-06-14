class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern is None or str is None:
            return False

        strlist = str.split()
        if len(strlist) != len(pattern):
            return False

        ptnDict = {}
        strDict = {}
        for i in range(len(strlist)):
            if strlist[i] not in strDict:
                strDict[strlist[i]] = pattern[i]
            if pattern[i] not in ptnDict:
                ptnDict[pattern[i]] = strlist[i]
            if strDict[strlist[i]] != pattern[i] or ptnDict[pattern[i]] != strlist[i]:
                return False

        return True

if __name__ == "__main__":
    sln = Solution()

    pattern = "abba"
    str = "dog cat cat fish"
    result = sln.wordPattern(pattern, str)
    print(result)

    pattern = "abba"
    str = "dog cat cat dog"
    result = sln.wordPattern(pattern, str)
    print(result)
