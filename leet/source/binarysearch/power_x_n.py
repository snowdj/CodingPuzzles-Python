class Solution():
    def myPow(self, x, n):
        # write your code here
        if x is None or n is None:
            return None

        if n == 0:
            return 1
        if n > 0:
            return self.pow(x, n)
        if n < 0:
            return 1.0 / self.pow(x, -n)

    def pow(self, x, n):
        result = 1
        tmp = x
        while n > 0:
            if n % 2 == 1:
                result *= tmp
            tmp *= tmp
            n = n // 2

        return result


if __name__ == "__main__":
    x = 2
    n = 5
    sln = Solution()
    result = sln.myPow(x, n)
    print(result)
    assert(result == 1024)