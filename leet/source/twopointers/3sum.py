class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or nums == []:
            return []
        
        result = []
        nums.sort()
        nlen = len(nums)
        leftval = None
        last_leftval = None
        for left in range(nlen):
            right0, right1 = left + 1, nlen - 1
            if leftval is not None:
                last_leftval = leftval
            leftval = nums[left]
            if leftval == last_leftval:
                continue

            while right0 < right1:
                curr_sum = leftval + nums[right0] + nums[right1]
                if curr_sum == 0:
                    result.append([leftval, nums[right0], nums[right1]])
                    right0 += 1
                    while right0 < right1 and nums[right0] == nums[right0-1]:
                        right0 += 1
                    right1 -= 1
                    while right1 > right0 and nums[right1] == nums[right1+1]:
                        right1 -= 1
                elif curr_sum < 0:
                    right0 += 1
                    while right0 < right1 and nums[right0] == nums[right0-1]:
                        right0 += 1
                else:
                    right1 -= 1
                    while right1 > right0 and nums[right1] == nums[right1+1]:
                        right1 -= 1
        
        return result

class Solution1:
    """faster"""
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s > 0:
                    r += -1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r += -1
                    l += 1
                    r -= 1
        return res

if __name__ == "__main__":
    sln = Solution()
    #res = sln.threeSum([-1, 1, 0, 0, 0])
    res = sln.threeSum([-2,0,0,2,2])
    print(res)