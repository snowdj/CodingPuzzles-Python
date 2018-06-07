class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k is None or n is None:
            return []

        if k == 0 or n == 0:
            return [[]]

        self.result = []
        self.dfs(k, n, 1, [])
        return self.result

    def dfs(self, k, n, startnum, nums):
        if k == 0 and n == 0 and nums not in self.result:
            self.result.append(nums[:])

        for i in range(startnum, 10):
            if i > n:
                return
            nums.append(i)
            self.dfs(k-1, n-i, i+1, nums)
            nums.pop()
