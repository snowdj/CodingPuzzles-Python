# eg. [1,2,2,4,5,5], target = 2
# eg. [1,2,2,4,5,5], target = 5

def lastPosition(nums, target):
    if nums is None or target is None:
        return -1

    start, end = 0, len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if target >= nums[mid]:
            start = mid
        elif target < nums[mid]:
            end = mid

    if nums[end] == target:
        return end
    if nums[start] == target:
        return start
    return -1