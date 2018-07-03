class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.range_type(nums, mid) == 0:
                return nums[mid]
            if self.range_type(nums, mid) == -1:
                start = mid
            else:
                end = mid

        if self.range_type(nums, start) == 0:
            return nums[start]
        return nums[end]

    def range_type(self, nums, pos):
        pos_left = max(0, pos-1)
        pos_right = min(len(nums) - 1, pos+1)
        if nums[pos] >= nums[pos_left] and nums[pos] >= nums[pos_right]:
            range_type = 0
        elif nums[pos] <= nums[pos_right]:
            range_type = -1
        else:
            range_type = 1
        return range_type

