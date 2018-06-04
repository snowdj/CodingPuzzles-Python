class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if n is None or k is None:
            return []

        self.result = []
        self.dfs(n, k, 0, [])
        return self.result

    def dfs(self, n, k, startpos, combination):
        if len(combination) == k and combination not in self.result:
            self.result.append(combination)

        for i in range(startpos, n):
            if len(combination) > k:
                return
            self.dfs(n, k, i+1, combination+[i+1])