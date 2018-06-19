class Solution():
    def permute(self, nums):
        if nums is None:
            return [[]]
        elif len(nums) <= 1:
            return [nums]

        result = []
        for i, item in enumerate(nums):
            #print("i={0}, item={1}".format(i, item))
            for p in permute(nums[:i] + nums[i + 1:]):
                #print("p={0}, item={1}, append {2}".format(p, item, p + [item]))
                result.append([item] + p)
                #print("now result is ... {0}".format(result))

        return result

class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        self.result = []
        visited = [False for i in nums]
        self.dfs(nums, visited, [])
        return self.result

    def dfs(self, nums, visited, permutation):
        if len(nums) == len(permutation):
            self.result.append(permutation[:])

        for i in range(0, len(nums)):
            if visited[i] == True:
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation)
            visited[i] = False
            permutation.pop()


if __name__ == "__main__":
    sln = Solution1()
    result = sln.permute([1, 5, 9])
    print(result)
