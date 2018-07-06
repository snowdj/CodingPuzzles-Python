class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or k is None:
            return None

        return self.quickSelect(nums, k, 0, len(nums) - 1)

    def quickSelect(self, nums, k, start, end):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[start + (end - start) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quickSelect(nums, k, start, right)
        if start + k - 1 >= left:
            return self.quickSelect(nums, k - (left - start), left, end)

        return nums[right+1]

if __name__ == "__main__":
    sln = Solution()
    res = sln.findKthLargest([3,2,1,5,6,4], 2)
    print(res)