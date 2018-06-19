class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0 or word is None:
            return False

        row = len(board)
        col = len(board[0])

        for x in range(row):
            for y in range(col):
                if self.search(x, y, 0, word, board):
                    return True

        return False

    def search(self, x, y, index, word, board):
        if not self.inbound(x, y, board):
            return False

        if word[index] != board[x][y]:
            return False

        if index == len(word) - 1:
            return True

        delta_x = [1, 0, -1, 0]
        delta_y = [0, 1, 0, -1]
        curr = board[x][y]
        board[x][y] = 0 # avoid visit the same grid for more than once, can also use an extra array to store this (visited[x][y])
        for i in range(4):
            new_x = x + delta_x[i]
            new_y = y + delta_y[i]
            if self.search(new_x, new_y, index+1, word, board):
                return True
        board[x][y] = curr
        return False

    def inbound(self, x, y, board):
        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):
            return True
        return False


class Solution1():
