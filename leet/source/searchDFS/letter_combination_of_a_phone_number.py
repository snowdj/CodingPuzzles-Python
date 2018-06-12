class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []

        self.dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        self.result = []
        self.search(digits, 0, [])
        return self.result

    def search(self, digits, index, combination):
        if len(digits) == len(combination):
            self.result.append("".join(x for x in combination))
            return

        for char in self.dict[digits[index]]:
            combination.append(char)
            self.search(digits, index+1, combination)
            combination.pop()

if __name__ == "__main__":
    sln = Solution()
    result = sln.letterCombinations("2")
    print(result)