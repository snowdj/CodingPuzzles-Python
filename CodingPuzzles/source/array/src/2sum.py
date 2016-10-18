def twoSum(nums, target):
    if nums is None or len(nums) == 0:
        return []

    for i in range(len(nums)):
        t_nums = nums[:]
        t_nums.pop(i)
        if (target - nums[i]) in t_nums:
            print("nums[i] = ", nums[i])
            print("target - nums[i] = ", target - nums[i])
            return [i+1, t_nums.index(target - nums[i])+2]

    return []

def twoSum2(nums, target):
    if nums is None or len(nums) == 0:
        return []

    tnums = []
    for i in range(len(nums)):
        if target - nums[i] in tnums:
            return [tnums.index(target - nums[i]) + 1, i+1] # keep the ascending order
        tnums.append(nums[i])

    return [-1, -1] # Note the condition when no solution is found

# This implementation is incorrect. It doesn't properly handle the duplicate values in nums.
def twoSum3(nums, target):
    if nums is None or len(nums) == 0:
        return []

    tnums = nums[:]
    tnums.sort()
    start = 0
    end = len(nums) - 1
    while start < end:
        if tnums[start] + tnums[end] == target:
            res = [nums.index(tnums[start])+1, nums.index(tnums[end])+1]
            res.sort()
            return res
        if tnums[start] + tnums[end] < target:
            start += 1
        else:
            end -= 1

    return [-1, -1]

def test_main():
    input_array = [2, 7, 11, 15]
    target = 9
    print("Test Data: ")
    print(input_array)
    print("Target: {0}".format(target))

    print("Test Result: twoSum")
    print(twoSum(input_array, target))
    print("Test Result: twoSum2")
    print(twoSum2(input_array, target))
    print("Test Result: twoSum3")
    print(twoSum3(input_array, target))


if __name__ == "__main__":
    test_main()