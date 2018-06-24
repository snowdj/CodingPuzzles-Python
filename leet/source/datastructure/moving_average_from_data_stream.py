class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        from collections import deque
        self.size = size
        self.nums = deque(maxlen=size)
        self.sum = None
    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        if len(self.nums) == 0:
            self.nums.append(val)
            avg = val * 1.0
            self.sum = avg * 1.0
            return avg

        if len(self.nums) < self.size:
            prelen = len(self.nums)
            presum = self.sum
            self.nums.append(val)
            self.sum += val
            avg = self.sum / (prelen + 1)
            return avg

        presum = self.sum
        k0 = self.nums.popleft()
        self.nums.append(val)
        self.sum = self.sum - k0 + val
        avg = self.sum / self.size
        return avg
