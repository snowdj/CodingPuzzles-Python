class Solution():
    def combination_sum(self, candidates, target):
        candidates = list(set(candidates)) # remove duplicated elements
        candidates.sort() # for early exit
        self.result = []
        self.dfs(candidates, target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, sub_result):
        length = len(candidates)
        if target == 0:
            return self.result.append(sub_result)
        for i in range(start, length):
            if target < candidates[i]:
                return # force early exit
            self.dfs(candidates, target - candidates[i], i, sub_result + [candidates[i]])

class Solution1():
    def combinationSum(self, candidates, target):
        # write your code here
        if candidates is None or len(candidates) == 0:
            return []

        self.result = []
        self.dfs(sorted(candidates), target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, sub_result):
        if target < 0:
            return

        if target == 0:
            self.result.append(sub_result[:]) # must use deep copy
            return

        length = len(candidates)
        for i in range(start, length):
            sub_result.append(candidates[i])
            # allow to use the number for any times, so start from i, not i+1
            self.dfs(candidates, target - candidates[i], i, sub_result)
            sub_result.pop()
