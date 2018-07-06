"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        if list1 is None or list1 == []:
            return list2
        if list2 is None or list2 == []:
            return list1

        def compare(interval0, interval1):
            if interval0.start < interval1.start:
                return -1
            elif interval0.start == interval1.start:
                return 0
            else:
                return 1

        result = []
        pos1, pos2 = 0, 0
        max1, max2 = len(list1), len(list2)
        start, end = None, None
        while pos1 < max1 and pos2 < max2:
            if compare(list1[pos1], list2[pos2]) <= 0:
                curr_interval = Interval(list1[pos1].start, list1[pos1].end)
                pos1 += 1
            else:
                curr_interval = Interval(list2[pos2].start, list2[pos2].end)
                pos2 += 1

            if start is None:
                start = curr_interval.start
                end = curr_interval.end
            else:
                if curr_interval.start <= end:
                    end = max(curr_interval.end, end)
                else:
                    result.append(Interval(start, end))
                    start = curr_interval.start
                    end = curr_interval.end

        while pos1 < max1:
            if list1[pos1].start <= end:
                end = max(list1[pos1].end, end)
            else:
                result.append(Interval(start, end))
                start = list1[pos1].start
                end = list1[pos1].end
            pos1 += 1

        while pos2 < max2:
            if list2[pos2].start <= end:
                end = max(list2[pos2].end, end)
            else:
                result.append(Interval(start, end))
                start = list2[pos2].start
                end = list2[pos2].end
            pos2 += 1

        result.append(Interval(start, end))
        return result

if __name__ == "__main__":
    sln = Solution()
    list1 = [Interval(1,2),Interval(3,4)]
    list2 = [Interval(2,3),Interval(5,6)]

    res = sln.mergeTwoInterval(list1, list2)
    for i in res:
        print((i.start, i.end))
    #assert(res == [Interval(1,4),Interval(5,6)])