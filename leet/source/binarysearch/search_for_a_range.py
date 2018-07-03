class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or nums == [] or target is None:
            return [-1, -1]

        # find the first position of target
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        left = -1
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [left, left]

        right = left
        while right < len(nums):
            if nums[right] == target:
                right += 1
            else:
                break

        return [left, right-1]

if __name__ == "__main__":
    sln = Solution()
    result = sln.searchRange([5, 7, 7, 8, 8, 10], 8)
    expected_result = [3, 4]
    assert(result == expected_result)