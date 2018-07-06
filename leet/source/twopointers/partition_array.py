class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if nums is None or len(nums) <= 1 or k is None:
            return 0

        pl, pr = 0, len(nums) - 1
        i = 0
        while i <= pr:
            if nums[i] < k:
                nums[pl], nums[i] = nums[i], nums[pl]
                pl += 1
                i += 1
            else:
                nums[pr], nums[i] = nums[i], nums[pr]
                pr -= 1

        return i

class Solution1:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if nums is None or len(nums) <= 1 or k is None:
            return 0

        left = 0
        right = len(nums) - 1
        while left < right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

if __name__ == "__main__":
    sln = Solution()
    res = sln.partitionArray([9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9], 9)
    print(res)