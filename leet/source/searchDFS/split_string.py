class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if s is None:
            return []

        if len(s) == 0:
            return [[]]

        self.result = []
        self.dfs(s, [])
        return self.result

    def dfs(self, s, strlist):
        if len(s) == 0:
            self.result.append(strlist)
            return

        for i in range(1,len(s)+1):
            #if len(s[:i]) > 2:
            if i > 2:
                continue
            self.dfs(s[i:], strlist+[s[:i]])

if __name__ == "__main__":
    str = "123"
    sln = Solution()
    result = sln.splitString(str)
    print(result)