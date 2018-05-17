def shortestPath_BFS(grid, source, destination):
    if not grid or not source or not destination:
        return -1

    m, n = len(grid), len(grid[0])
    visited = set()
    delta_x = [1, 1, -1, -1, 2, 2, -2, -1]
    delta_y = [2, -2, 2, -2, 1, -1, 1, -1]
    queue = [(source.x, source.y, 0)]

    while len(queue):
        size = len(queue)
        for i in range(size):
            x, y, pathLen = queue[0]
            del queue[0]
            if x == destination.x and y == destination.y:
                return pathLen

            for k in range(8):
                nx = x + delta_x[k]
                ny = y + delta_y[k]
                if check(grid, m, n, nx, ny, visited):
                    queue.append((nx, ny, pathLen + 1))
                    visited.add((nx, ny))

    return -1

def check(grid, m, n, x, y, visited):
    #m, n = len(grid), len(grid[0])
    if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in visited and grid[x][y] == 0:
        return True
    return False

def shortestPath_BiBFS(grid, source, destination):
