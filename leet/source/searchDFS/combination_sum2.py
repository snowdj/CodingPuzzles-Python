class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        if num is None or len(num) == 0 or target is None:
            return []

        num.sort()
        self.result = []
        self.dfs(num, target, 0, [])
        return self.result

    def dfs(self, num, target, startpos, combination):
        if target == 0:
            if combination not in self.result:
                self.result.append(combination)

        for i in range(startpos, len(num)):
            if num[i] > target:
                return
            self.dfs(num, target - num[i], i+1, combination+[num[i]])
