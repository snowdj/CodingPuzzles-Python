def twoSum(nums, target):
    if nums is None or target is None or len(nums) <= 1:
        return []

    for i in range(0, len(nums) - 1):
        for j in range(i+1, len(nums)):
            print("i={0}, j={1}").format(i, j)
            #if nums[i] + nums[j] == target:
                #return [i, j]

    return []

def twoSum1(nums, target):
    mem = {}
    for i in range(len(nums)):
        if (target - nums[i]) in mem:
            return [mem[target - nums[i]], i]
        mem[nums[i]] = i

    return []

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    target = 6
    result = twoSum1(nums, target)
    print(result)

