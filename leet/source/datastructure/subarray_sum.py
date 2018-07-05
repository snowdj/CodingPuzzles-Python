class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []

        presum = [0]
        history = {}
        for i, n in enumerate(nums):
            curr_presum = presum[i] + n
            presum.append(curr_presum)
            if curr_presum in history:
                result = [history[curr_presum]+1, i]
                return result
            history[curr_presum] = i

        return []

class Solution1():
    def subarraySum(self, nums):
        hs = {0:-1}
        sum = 0
        for i in range(len(nums)):
            # if A[i] == 0:
            #     return [i, i]
            sum += nums[i]
            if sum in hs:
                return [hs[sum] + 1, i]
            hs[sum] = i
        return

if __name__ == "__main__":
    sln = Solution()
    res = sln.subarraySum([-3,1,2,-3,4])
    print(res)