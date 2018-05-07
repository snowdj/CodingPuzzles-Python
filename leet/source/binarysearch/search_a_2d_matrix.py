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

if __name__ == "__main__":
    