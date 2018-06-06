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

        self.exist = [False for i in range(n+1)]
        self.exist[0] = True # skip number 0
        self.dfs(n, str, 0)
        for i, v in enumerate(self.exist):
            if v == False:
                return i

        return None


    def dfs(self, n, str, startpos):
        if len(str) == 0:
            return

        for i in range(1, len(str) + 1):
            if int(str[:i]) >= 1 and int(str[:i]) <= n:
                if self.exist[int(str[:i])] is False:
                    self.exist[int(str[:i])] = True
                self.dfs(n, str[i:], i+1)
            else:
                continue


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

class Solution3:
# Workable solution
    # @param {int} n an integer
    # @param {string} str a string with number from 1-n
    #                     in random order and miss one number
    # @return {int} an integer
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        return self.find(n, str, 0, used)

    def find(self, n, str, index, used):
        if index == len(str):
            results = []
            for i in range(1, n + 1):
                if not used[i]:
                    results.append(i)
            return results[0] if len(results) ==1 else -1

        if str[index] == '0':
            return -1

        for l in range(1, 3):
            num = int(str[index : index + l])
            if num >=1 and num <= n and not used[num]:
                used[num] = True
                target = self.find(n, str, index + l, used)
                if target != -1:
                    return target
                used[num] = False

        return -1

if __name__ == "__main__":
    sln = Solution()
    n = 20
    str = "19201234567891011121314151618"
    #n = 20
    #str = "19201"
    result = sln.findMissing2(n, str)
    print(result)



