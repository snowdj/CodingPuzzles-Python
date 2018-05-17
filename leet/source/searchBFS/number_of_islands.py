# BFS
class SolutionBFS:
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]

        count = 0
        for row in range(m):
            for col in range(n):
                if self.shouldCheck(row, col, grid, visited):
                    visited[row][col] = True
                    visited = self.bfs(row, col, visited)
                    count += 1

        return count

    def bfs(self, x, y, row, col, grid, visited):
        nbrow = [1, 0, -1, 0]
        nbcol = [0, 1, 0, -1]
        q = [(x, y)]
        while len(q) > 0:
            x = q[0][0]
            y = q[0][1]
            q.pop(0)
            for k in range(4):
                newx = x + nbrow[k]
                newy = y + nbcol[k]
                if self.shouldCheck(newx, newy, row, col, grid, visited):
                    visited[newx][newy] = True
                    q.append((newx, newy))

        return visited

    def shouldCheck(self, x, y, row, col, grid, visited):
        if x >= 0 and x < row and y >= 0 and y < col and grid[x][y] == 1 and visited[x][y] == False:
            return True
        return False

# DFS
class SolutionDFS:
    def numIslands(self, grid):
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)] for j in range(m)]

        def shouldCheck(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1 and visited[x][y] == False:
                return True
            return False

        def dfs(x, y):
            delta_x = [1, 0, -1, 0]
            delta_y = [0, 1, 0, -1]
            for k in range(4):
                newx = x + delta_x[k]
                newy = y + delta_y[k]
                if shouldCheck(newx, newy):
                    visited[newx][newy] = True
                    dfs(newx, newy)

        count = 0
        for row in range(m):
            for col in range(n):
                if shouldCheck(row, col):
                    visited[row][col] = True
                    dfs(row, col)
                    count += 1

        return count