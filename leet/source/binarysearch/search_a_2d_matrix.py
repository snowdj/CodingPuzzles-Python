class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0 or target is None:
            return False

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return target == matrix[0][0]

        start, end = 0, len(matrix)
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                end = mid
            else:
                start = mid

        if target < matrix[end][0]:
            s1, e1 = 0, len(matrix[start])
            while (s1 + 1 < e1):
                mid = s1 + (e1 - s1) // 2
                if target == matrix[start][mid]:
                    return True
                if target < matrix[start][mid]:
                    e1 = mid
                else:
                    s1 = mid
            if matrix[start][s1] == target or matrix[start][e1] == target:
                return True
            return False
        else:
            s1, e1 = 0, len(matrix[end])
            while (s1 + 1 < e1):
                mid = s1 + (e1 - s1) // 2
                if target == matrix[end][mid]:
                    return True
                if target < matrix[end][mid]:
                    e1 = mid
                else:
                    s1 = mid
            if matrix[end][s1] == target or matrix[end][e1] == target:
                return True
            return False

class Solution1:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or matrix == [] or matrix == [[]] or target is None:
            return False

        target_row_id = None
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.in_row(matrix[mid], target) == 0:
                target_row_id = mid
                break
            if self.in_row(matrix[mid], target) == -1:
                start = mid
            else:
                end = mid

        if target_row_id is None:
            if self.in_row(matrix[start], target) == 0:
                target_row_id = start
            elif self.in_row(matrix[end], target) == 0:
                target_row_id = end
            else:
                return False

        curr_row = matrix[target_row_id]
        c_start, c_end = 0, len(curr_row) - 1
        while c_start + 1 < c_end:
            mid = c_start + (c_end - c_start) // 2
            if curr_row[mid] == target:
                return True
            if curr_row[mid] < target:
                c_start = mid
            else:
                c_end = mid

        if curr_row[c_start] == target or curr_row[c_end] == target:
            return True
        return False

    def in_row(self, row, target):
        result = 0
        if row[0] <= target and row[-1] >= target:
            result = 0
        elif row[-1] < target:
            result = -1
        else:
            result = 1
        return result

class Solution2:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        n, m = len(matrix), len(matrix[0])
        start, end = 0, n * m - 1
        while start + 1 < end:
            mid = (start + end) / 2
            x, y = mid / m, mid % m
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid
        x, y = start / m, start % m
        if matrix[x][y] == target:
            return True

        x, y = end / m, end % m
        if matrix[x][y] == target:
            return True

        return False

if __name__ == "__main__":
    sln = Solution1()
    result = sln.searchMatrix([[1],[3],[5]], 3)
    print(result)