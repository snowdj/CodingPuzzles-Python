class Solution():
    def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        store = [[],[],[]]
        for i in nums:
            store[i].append(i)

        return store[0]+store[1]+store[2]

class Solution1():
    def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        n = Counter(nums)
        nums = [0 for k in range(n[0])] + [1 for k in range(n[1])] + [2 for k in range(n[2])]
        print(nums)

class Solution2():
    def sortColors(nums):
        cnt = {}
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
        nums = [0 for k in range(cnt[0])] + [1 for k in range(cnt[1])] + [2 for k in range(cnt[2])]

class Solution3():
    def sortColors3(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            pass

        def swap(nums, p_s, p_d):
            if nums is None or len(nums) <= 1:
                return nums

            if p_s >= 0 and p_s <= len(nums) - 1 and p_d >= 0 and p_d <= len(nums) - 1:
                nums[p_s], nums[p_d] = nums[p_d], nums[p_s]

            return nums

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

class Solution4:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return

        pl = 0
        pr = len(nums) - 1
        i = 0
        while i <= pr:
            if nums[i] == 0:
                nums[i], nums[pl] = nums[pl], nums[i]
                pl += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[pr] = nums[pr], nums[i]
                pr -= 1

        return nums

class Solution5:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        s, e, l = 0, 0 , len(nums) - 1

        while e <= l:
            if nums[e] < pivot:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e += 1
            elif nums[e] == pivot:
                e += 1
            else:
                nums[l], nums[e] = nums[e], nums[l]
                l -= 1


if __name__ == "__main__":
    sln = Solution4()
    #test_nums = [1,0]
    test_nums = [1,2,0]

    res = sln.sortColors(test_nums)
    print(res)
