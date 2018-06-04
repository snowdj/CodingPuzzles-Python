class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        if n == 0:
            return 0

        if str is None:
            return 1

        self.numstrs = []
        self.dfs(n, str, [])
        return self.findmissing(self.numstrs, n)

    def dfs(self, n, str, numlist):
        if len(str) == 0 and sorted(numlist) not in self.numstrs:
            self.numstrs.append(sorted(numlist))

        for i in range(1, len(str) + 1):
            if len(str[:i]) > 2 or int(str[:i]) > n:
                continue
            self.dfs(n, str[i:], numlist+[str[:i]])

    def findmissing(self, numstrs, n):
        record = [0 for i in range(n+1)]
        record[0] = 1 # skip number 0 as it does not exist in the n numbers
        for nums in numstrs:
            for n in nums:
                record[int(n)] = 1

        return record.index(0)


class Solution2:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        if n == 0:
            return 0

        if str is None:
            return 1

        self.visit = [False for i in range(n+1)]
        self.numstrs = []
        self.dfs(n, str, [])
        return self.findmissing(self.numstrs, n)

    def dfs(self, n, str, numlist):
        if len(str) == 0 and sorted(numlist) not in self.numstrs:
            self.numstrs.append(sorted(numlist))

        for i in range(1, len(str) + 1):
            if len(str[:i]) > 2 or int(str[:i]) > n:
                continue
            self.dfs(n, str[i:], numlist+[str[:i]])

    def findmissing(self, numstrs, n):
        record = [0 for i in range(n+1)]
        record[0] = 1 # skip number 0 as it does not exist in the n numbers
        for nums in numstrs:
            for n in nums:
                record[int(n)] = 1

        return record.index(0)


if __name__ == "__main__":
    sln = Solution()
    n = 20
    str = "19201234567891011121314151618"
    result = sln.findMissing2(n, str)
    print(result)

