class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        n = nums[0]
        for i in nums[1:]:
            n = i ^ n

        return n