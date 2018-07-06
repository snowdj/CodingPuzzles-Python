class Solution():
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if B is None or n == 0:
            return

        if A is None or m == 0:
            A[:] = B[:]

        pos = m + n - 1
        posA = m - 1
        posB = n - 1
        while posA >= 0 and posB >= 0:
            if A[posA] > B[posB]:
                A[pos] = A[posA]
                posA -= 1
            else:
                A[pos] = B[posB]
                posB -= 1
            pos -= 1

        if posB >= 0:
            A[:pos+1] = B[:posB+1]

        return A

if __name__ == "__main__":
    sln = Solution()

    # A = [1, 2, 3, None, None]
    # m = 3
    # B = [4, 5]
    # n = 2

    # A = [9, 10, 11, 12, 13, None, None, None, None]
    # m = 5
    # B = [4, 5, 6, 7]
    # n = 4

    A = [None, None, None, None]
    m = 0
    B = [4, 5, 6, 7]
    n = 4

    res = sln.mergeSortedArray(A, m, B, n)
    print(res)