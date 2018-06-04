class Solution():
# Start from prefix
    def wordBreak(self, s, wordDict):
        if len(wordDict) == 0:
            return []

        self.result = []
        self.mem = {}
        return self.dfs(s, wordDict)

    def dfs(self, s, wordDict):
        if s in self.mem: return self.mem[s]

        result = []

        if len(s) == 0:
            return result

        if s in wordDict:
            result.append(s)
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            suffix = s[i:]
            right_wordlist = self.dfs(suffix, wordDict)

            for w in right_wordlist:
                result.append(prefix + ' ' + w)

        self.mem[s] = result
        return result

class Solution1():
# Start from suffix
    def wordBreak(self, s, wordDict):
        if len(wordDict) == 0:
            return []

        self.result = []
        self.mem = {}
        return self.dfs(s, wordDict)

    def dfs(self, s, wordDict):
        if s in self.mem: return self.mem[s]

        result = []

        if len(s) == 0:
            return result

        if s in wordDict:
            result.append(s)

        for i in range(1, len(s)):
            suffix = s[i:]
            if suffix not in wordDict:
                continue

            prefix = s[:i]
            left_wordlist = self.dfs(prefix, wordDict)
            for w in left_wordlist:
                result.append(w, " ", suffix)

        self.mem[s] = result
        return result

if __name__ == "__main__":
    sln = Solution()
    result = sln.wordBreak("leetcode", ['leet', 'code'])
    print(result)
