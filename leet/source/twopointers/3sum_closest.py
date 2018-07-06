class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or target is None:
            return []

        nums.sort()
        minsum = None
        import sys
        mindiff = sys.maxsize
        for left in range(len(nums) - 2):
            l, r = left + 1, len(nums) - 1
            while l < r:
                csum = nums[left] + nums[l] + nums[r]
                if csum == target:
                    return csum
                if csum < target:
                    l += 1
                else:
                    r -= 1
                if abs(csum - target) < mindiff:
                    mindiff = abs(csum - target)
                    minsum = csum

        return minsum

if __name__ == "__main__":
    sln = Solution()
    #res = sln.threeSumClosest([-1,2,1,-4], 1)
    #res = sln.threeSumClosest([1,1,1,0], -100)
    res = sln.threeSumClosest([0,2,1,-3], 1)
    print(res)