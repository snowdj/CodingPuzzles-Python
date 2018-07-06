# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    """Beats 99%"""
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if intervals is None or len(intervals) == 0:
            return True

        intervals.sort(key=lambda a: a.start)
        end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                return False
            end = intervals[i].end

        return True

class Solution1:
    """Beats 100%"""
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals)<=1:
            return True

        intervals = sorted(intervals, key = lambda a: a.start)
        d = intervals.pop(0)
        end_time = d.end

        for k in intervals:
            if k.start<end_time:
                return False
            end_time = k.end
        return True

if __name__ == "__main__":
    sln = Solution()
    res = sln.canAttendMeetings([Interval(0,30),Interval(5,10),Interval(15,20)])
    print(res)
