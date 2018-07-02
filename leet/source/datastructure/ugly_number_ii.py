class Solution():
    """brute force"""
    def nthUglyNumber(self, n):
        import sys
        nums = []
        for a in range(1, sys.maxsize):
            #if len(nums) >= n:
            #    break
            a *= 2
            for b in range(a, sys.maxsize):
                #if len(nums) >= n:
                #    break
                b *= 3
                for c in range(b, sys.maxsize):
                    c *= 5
                    nums.append(c)
                    #if len(nums) >= n:
                    #    break
        nums.sort()
        return nums[n-1]

class Solution1():
    """O(n) scan"""
    def nthUglyNumber(self, n):
        nums = [1]
        i = 0
        p2 = p3 = p5 = 0
        while i < n:
            next = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            nums.append(next)
            if next == nums[p2] * 2:
                p2 += 1
            if next == nums[p3] * 3:
                p3 += 1
            if next == nums[p5] * 5:
                p5 += 1
            i += 1
        return nums[n-1]

class Solution2():
    """O(nLogn) hash + heap"""
    def nthUglyNumber(self, n):
        import heapq
        if n <= 1:
            return n

        n -= 1
        key = [2, 3, 5]
        h = []
        for i in range(3):
            heapq.heappush(h, (key[i], i))

        value = key[0]
        while n > 0:
            value, level = heapq.heappop(h)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            n -= 1
        return value

if __name__ == "__main__":
    sln = Solution1()
    res = sln.nthUglyNumber(9)
    print(res)