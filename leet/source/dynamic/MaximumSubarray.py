def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    dp = [0 for k in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i-1] < 0:
            dp[i] = nums[i]
        else:
            dp[i] = dp[i - 1] + nums[i]

    return max(dp)

if __name__ == "__main__":
    test_nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = maxSubArray(test_nums)
    print(res)
