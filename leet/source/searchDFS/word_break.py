class Solution:
    # Leetcode Accepted
    # Lintcode Time Limit Exceeded
    def wordBreak(self, s, dict):
        if len(dict) == 0:
            return len(s) == 0

        self.mem = {}
        return self.couldBreak(s, dict)

    def couldBreak(self, s, dict):
        if s in self.mem:
            return self.mem[s]

        if s in dict:
            self.mem[s] = True
            return self.mem[s]

        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            if right in dict and self.couldBreak(left, dict):
                self.mem[s] = True
                return self.mem[s]

        self.mem[s] = False
        return self.mem[s]

class Solution1:
    # Leetcode Accepted
    # Lintcode Time Limit Exceeded
    def wordBreak(self, s, dict):
        def canBreak(s, m, dict):
            if s in m: return m[s]
            if s in dict:
                m[s] = True
                return True

            for i in range(1, len(s)):
                r = s[i:]
                if r in dict and canBreak(s[:i], m, dict):
                    m[s] = True
                    return True

            m[s] = False
            return False

        return canBreak(s, {}, set(dict))