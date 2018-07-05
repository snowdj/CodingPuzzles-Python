class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None

        import sys
        maxsum = -sys.maxsize
        minsum = 0
        tsum = 0
        for n in nums:
            tsum += n
            maxsum = max(maxsum, tsum - minsum)
            minsum = min(tsum, minsum)

        return maxsum

