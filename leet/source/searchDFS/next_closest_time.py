class Solution():
    def nextClosestTime(self, timestr):
        if timestr is None or len(timestr) == 0:
            return timestr

        nums = []
        for i in range(len(timestr)):
            if timestr[i] != ":":
                nums.append(timestr[i])

        #nums = set(nums)
        if len(nums) == 1:
            return timestr

        import sys
        self.diff = sys.maxsize
        self.result = []
        minute = int(timestr[0:2]) * 60 + int(timestr[3:5])
        self.search(nums, "", 0, minute)
        print(self.result)
        #resulttime = self.result[0:2] + ":" + self.result[3:5]
        #return resulttime

    def search(self, nums, currtime, index, target):
        if index == 4:
            m = int(currtime[0:2]) * 60 + int(currtime[2:4])
            if m == target:
                return
            if m - target > 0:
                d = m - target
            else:
                d = 1440 + m - target # 24hour * 60min = 1440 min
            if d < self.diff:
                self.diff = d
                self.result = currtime
            return

        for i in range(0, len(nums)):
            if index == 0 and int(nums[i]) > 2:
                continue
            if index == 1 and int(currtime) * 10 + int(nums[i]) > 23:
                continue
            if index == 2 and int(nums[i]) > 5:
                continue
            if index == 3 and int(currtime[2]) * 10 + int(nums[i]) > 59:
                continue
            self.search(nums, currtime + nums[i], index+1, target)


if __name__ == "__main__":
    sln = Solution()
    timestr = "19:34"
    result = sln.nextClosestTime(timestr)
    print(result)
