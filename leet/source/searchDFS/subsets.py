class Solution1():
    def subsets(self, S):
        def dfs(depth, start, valuelist):
            #print("depth={0}, start={1}, valuelist={2}".format(depth, start, valuelist))
            if len(valuelist) > 0:
                print("append {}".format(valuelist))
                res.append(valuelist)

            if depth == len(S):
                print("time to return")
                return

            for i in range(start, len(S)):
                print("depth={}, start={}, i={}".format(depth, start, i))
                dfs(depth+1, i+1, valuelist+[S[i]])

        S.sort()
        res = []
        dfs(0, 0, [])
        return res

class Solution2():
    def subsets(self, nums):
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        self.res = []
        nums.sort()
        self.dfs(nums, [], 0)
        return self.res

    def dfs(self, nums, level_result, i):
        self.res.append(level_result[:])
        for n in nums:
            level_result.append(n)
            self.dfs(nums, level_result, i+1)
            nums.pop()

class Solution2a():
    def subsets(self, nums):
        self.res = []
        self.dfs(nums, [], 0)

    def dfs(self, nums, temp, i):
        self.res.append(temp[:])
        for k in range(i, len(nums)):
            temp.append(nums[k])
            self.dfs(nums, temp, k+1)
            temp.pop()

class Solution2b(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        self.result = []
        self.dfs(nums, 0, [])
        return self.result

    def dfs(self, nums, startpos, sub_result):
        self.result.append(sub_result)
        for i in range(startpos, len(nums)):
            self.dfs(nums, i+1, sub_result+[nums[i]])


if __name__ == "__main__":
    sln = Solution1()
    print(sln.subsets([1, 5, 9]))