import sys

def twoSumCloset(nums, target):
    if nums is None or len(nums) == 0:
        return target

    nums.sort()
    diff = sys.maxsize
    start = 0
    end = len(nums) - 1
    while start < end:
        if nums[start] + nums[end] < target:
            diff = min(diff, target - (nums[start] + nums[end]))
            start += 1
        elif nums[start] + nums[end] > target:
            diff = min(diff, nums[start] + nums[end] - target)
            end -= 1
        else:
            diff = 0
            return diff

    return diff


def test_main():
    nums = [-1, 2, 1, -4]
    target = 4
    print(twoSumCloset(nums, target))

    nums = [-1, 2, 1, -4]
    target = 3
    print(twoSumCloset(nums, target))


if __name__ == "__main__":
    test_main()
