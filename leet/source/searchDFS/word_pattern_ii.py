class Solution():
    # Based on Word Pattern I, but need split the words using DFS to try all possibilities
    def wordPatternMatch(self, pattern, str):
        record_map = {}
        record_set = set()
        return self.match(pattern, str, record_map, record_set)

    def match(self, pattern, str, record_map, record_set):
        if len(pattern) == 0:
            return len(str) == 0

        c = pattern[0]
        if c in record_map:
            mapped_str = record_map.get(c)
            if not str.startswith(mapped_str):
                return False

            return self.match(pattern[1:], str[len(mapped_str):], record_map, record_set)

        for i in range(len(str)):
            word = str[:i+1]
            if word in record_set:
                continue
            record_map[c] = word
            record_set.add(word)
            if self.match(pattern[1:], str[i+1:], record_map, record_set):
                return True
            record_set.remove(word)
            del record_map[c]

        return False


class Solution2(object):

    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d, used = {}, {}
        return self.match(pattern, str, d, used)


    def match(self, pattern, str, d, used):
        if len(pattern) == 0 and len(str) == 0:
            return True
        elif len(pattern) == 0 or len(str) == 0:
            return False

        if len(pattern) == 1:
            if pattern in d:
                if d[pattern] == str:
                    return True
                else:
                    return False
            else:
                if str in used and used[str]:
                    return False
                else:
                    return True

        if pattern[0] in d:
            if str.find(d[pattern[0]]) != 0:
                return False
            else:
                result = self.match(pattern[1:], str[len(d[pattern[0]]):], d, used)
                if result:
                    return True
        else:
            length = len(str) - (len(pattern) - 1)
            for i in range(length):
                cur = str[:i+1]
                if cur in used and used[cur]:
                    continue
                used[cur] = True
                d[pattern[0]] = cur
                result = self.match(pattern[1:], str[len(cur):], d, used)
                del d[pattern[0]]
                if result:
                    return True
                del used[cur]

        return False

if __name__ == "__main__":
    sln = Solution()

    pattern = "abab"
    str = "redblueredblue"
    result = sln.wordPatternMatch(pattern, str)
    print(result)
