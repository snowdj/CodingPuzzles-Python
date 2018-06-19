class Solution():
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.cols = [0 for i in range(n)]
        self.diag1 = [0 for i in range(2 * n - 1)]
        self.diag2 = [0 for i in range(2 * n - 1)]
        self.result = 0
        self.search(n, 0)
        return self.result

    def search(self, n, row):
        if row == n:
            self.result += 1

        for col in range(n):
            if not self.available(col, row, n):
                continue
            self.update_board(col, row, n, True)
            self.search(n, row+1)
            self.update_board(col, row, n, False)

    def available(self, x, y, n):
        if not self.cols[x] and not self.diag1[x+y] and not self.diag2[x-y+n-1]:
            return True
        return False

    def update_board(self, x, y, n, value):
        self.cols[x] = value
        self.diag1[x+y] = value
        self.diag2[x-y+n-1] = value

if __name__ == "__main__":
    sln = Solution()
    result = sln.totalNQueens(4)
    print(result)
