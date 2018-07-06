# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)

        room = 1
        intervals.sort(key=lambda a: a.start)
        first = intervals.pop(0)
        start, end = first.start, first.end
        for i in intervals:
            if i.start <= end:
                end = max(end, i.end)
                room += 1
            else:
                start = i.start
                end = i.end

        return room


if __name__ == "__main__":
    sln = Solution()
    #res = sln.minMeetingRooms([Interval(7,10),Interval(2,4)])
    res = sln.minMeetingRooms([Interval(0,30),Interval(5,10),Interval(15,20)])

    print(res)
