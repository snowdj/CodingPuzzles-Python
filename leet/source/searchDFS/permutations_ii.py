class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        nums.sort()
        self.result = []
        visited = [False for i in nums]
        self.dfs(nums, visited, [])
        return self.result

    def dfs(self, nums, visited, permutation):
        if len(nums) == len(permutation):
            self.result.append(permutation[:])

        for i in range(len(nums)):
            if visited[i] == True:
                continue

            if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation)
            visited[i] = False
            permutation.pop()


if __name__ == "__main__":
    input = [1, 1, 2]
    sln = Solution()
    result = sln.permuteUnique(input)
    print(result)