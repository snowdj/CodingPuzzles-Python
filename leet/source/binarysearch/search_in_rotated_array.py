class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or target is None:
            return -1

        def get_range(n):
            if nums[0] < nums[-1]:
                return 1
            if n >= nums[0]:
                return 1
            return 0

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            if get_range(nums[mid]) == 1:
                if target > nums[mid]:
                    start = mid
                else:
                    if get_range(target) == 1:
                        end = mid
                    else:
                        start = mid
            else:
                if target > nums[mid]:
                    if get_range(target) == 1:
                        end = mid
                    else:
                        start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == "__main__":
    sln = Solution()

    result = sln.search([5,1,3], 3)
    print(result)

    result = sln.search([4,5,6,7,0,1,2], 6)
    print(result)

    result = sln.search([4,5,6,7,0,1,2], 0)
    print(result)

    result = sln.search([3,5,1], 1)