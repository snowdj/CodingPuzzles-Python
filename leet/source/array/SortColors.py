def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    store = [[],[],[]]
    for i in nums:
        store[i].append(i)

    return store[0]+store[1]+store[2]

def sortColors1(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    from collections import Counter
    n = Counter(nums)
    nums = [0 for k in range(n[0])] + [1 for k in range(n[1])] + [2 for k in range(n[2])]
    print(nums)

def sortColors2(nums):
    cnt = {}
    for i in nums:
        cnt[i] = cnt.get(i, 0) + 1
    nums = [0 for k in range(cnt[0])] + [1 for k in range(cnt[1])] + [2 for k in range(cnt[2])]


def swap(nums, p_s, p_d):
    if nums is None or len(nums) <= 1:
        return nums

    if p_s >= 0 and p_s <= len(nums) - 1 and p_d >= 0 and p_d <= len(nums) - 1:
        nums[p_s], nums[p_d] = nums[p_d], nums[p_s]

    return nums

def sortColors3(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if nums is None or len(nums) <= 1:
        pass

    p_red = 0
    p_blue = len(nums) - 1
    while nums[p_red] == 0 and p_red < len(nums) - 1:
        p_red += 1
    while nums[p_blue] == 2 and p_blue > 0:
        p_blue -= 1

    i = p_red
    while (i <= p_blue):
        if nums[i] == 0:
            nums = swap(nums, i, p_red)
            p_red += 1
        if nums[i] == 2:
            nums = swap(nums, i, p_blue)
            p_blue -= 1
        else:
            i += 1

    print(nums)

if __name__ == "__main__":
    #test_nums = [1,0]
    test_nums = [1,2,0]
    sortColors3(test_nums)

