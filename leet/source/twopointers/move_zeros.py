class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return []

        pos, zero = 0, 0
        while pos < len(nums) - 1 and zero < len(nums):
            if nums[pos] != 0:
                pos += 1
                zero += 1
            else:
                while zero < len(nums) - 1 and nums[zero] == 0:
                    zero += 1
                nums[pos], nums[zero] = nums[zero], nums[pos]
                pos += 1
                zero += 1

        return nums

class Solution1():
    def moveZeroes(self, nums):
        pos = 0
        index = 0
        while index < len(nums):
            if nums[index] != 0:
                nums[pos] = nums[index]
                pos += 1

            index += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1


if __name__ == "__main__":
    sln = Solution1()
    res = sln.moveZeroes([0,1,0,3,12])
    print(res)
