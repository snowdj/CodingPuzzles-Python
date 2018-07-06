class Solution():
    def subarraySum(nums):

        for i in range(len(nums)):
            if nums[i] == 0:
                return [i, i]

            sum = nums[i]

            for j in range(i+1, len(nums)):
                sum += nums[j]
                if sum == 0:
                    return [i, j]

        return []


if __name__ == "__main__":
    input_array = [-3, 1, 2, -3, 4];
    res = subarraySum(input_array)
