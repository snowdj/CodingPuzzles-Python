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


class Solution1:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if nums is None:
            return []

        if len(nums) == 0:
            return [[]]

        nums.sort()
        visited = [False for i in range(len(nums))]
        self.result = []
        self.dfs(nums, visited, [])
        return self.result

    def dfs(self, nums, visited, permutation):
        if len(permutation) == len(nums):
            self.result.append(permutation)

        for i in range(0, len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and visited[i-1] is False:
                continue

            visited[i] = True
            self.dfs(nums, visited, permutation + [nums[i]])
            visited[i] = False

if __name__ == "__main__":
    input = [1, 1, 2]
    sln = Solution()
    result = sln.permuteUnique(input)
    print(result)