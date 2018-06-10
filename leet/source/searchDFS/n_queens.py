class Solution():
    def __init__(self):
      self.board = []
      self.cols = []
      self.diag1 = []
      self.diag2 = []
      self.result = []

    def solve_nqueens(self, n):
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag1 = [0 for i in range(2 * n - 1)]
        self.diag2 = [0 for i in range(2 * n - 1)]

        self.search(n, 0)
        return self.result

    def search(self, n, row):
        if row == n:
            temp = []
            for r in self.board:
                tstr = ""
                for c in r:
                    tstr += ",".join(c)
                temp.append(tstr)
            self.result.append(temp)
            return

        for col in range(0, n):
            if not self.available(col, row, n):
                continue
            self.update_board(col, row, n, True)
            self.search(n, row + 1)
            self.update_board(col, row, n, False)

    def available(self, x, y, n):
        if not self.cols[x] and not self.diag1[x+y] and not self.diag2[x-y+n-1]:
            return True
        return False

    def update_board(self, x, y, n, value):
        self.cols[x] = value
        self.diag1[x+y] = value
        self.diag2[x-y+n-1] = value
        if value is True:
            self.board[y][x] = 'Q'
        else:
            self.board[y][x] = '.'


class Solution1:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens.
    @return: All distinct solutions.
    """
    n = 0
    results = []
    cols = {}

    def attack(self, row, col):
        for c, r in self.cols.iteritems():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row):
        if row == self.n:
            result = []
            for i in range(self.n):
                r = ['.'] * self.n
                r[self.cols[i]] = 'Q'
                result.append(''.join(r))
            self.results.append(result)
            return

        for col in range(self.n):
            if col in self.cols:
                continue
            if self.attack(row, col):
                continue
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col]

    def solveNQueens(self, n):
        self.n = n
        self.search(0)
        return self.results


if __name__ == "__main__":
    sln = Solution()
    result = sln.solve_nqueens(4)
    print(result)