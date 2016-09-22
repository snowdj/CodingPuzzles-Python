def twoSum(nums, target):
    if nums is None or len(nums) < 2:
        return []

    for i in range(len(nums)):
        t_nums = nums[:]
        t_nums.pop(i)
        if (target - nums[i]) in t_nums:
            print("nums[i] = ", nums[i])
            print("target - nums[i] = ", target - nums[i])
            return [i+1, t_nums.index(target - nums[i])+2]

    return []

def test():
    input_array = [2, 7, 11,15]
    target = 9
    print "Test Data: "
    print input_array
    print("Target: {0}".format(target))

    print "Test Result: "
    print twoSum(input_array, target)

if __name__ == "__main__":
    test()