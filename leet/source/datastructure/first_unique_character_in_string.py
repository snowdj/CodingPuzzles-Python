class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        if str is None:
            return None

        from collections import OrderedDict
        record = OrderedDict()
        for i in str:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1

        for k, v in record.items():
            if v == 1:
                return k

        return None

class Solution1():
    def firstUniqChar(self, str):
        char = [0 for i in range(256)]

        for i in str:
            char[ord(i)] += 1

        for i in str:
            if char[ord(i)] == 1:
                return i


if __name__ == "__main__":
    sln = Solution()

    #input = "abaccdeff"
    #res = sln.firstUniqChar(input)
    #print(res)

    input = "absd"
    res = sln.firstUniqChar(input)
    print(res)