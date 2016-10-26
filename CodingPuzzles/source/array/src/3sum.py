def threeSum(nums):
    if nums is None or len(nums) == 0:
        return []

    nums.sort()
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == 0:
            return [start, end]
        if nums[start]