"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if intervals is None or len(intervals) <= 1:
            return intervals

        result = []
        import heapq
        heap = []
        for i, inter in enumerate(intervals):
            if len(inter) == 0:
                continue
            heapq.heappush(heap, (inter[0].start, inter[0].end, i, 0))

        start, end = None, None
        while len(heap) > 0:
            inter_start, inter_end, n, pos = heapq.heappop(heap)
            if start is None:
                start = inter_start
                end = inter_end
            else:
                if inter_start <= end:
                    end = max(inter_end, end)
                else:
                    result.append(Interval(start, end))
                    start = inter_start
                    end = inter_end
            if pos < len(intervals[n]) - 1:
                heapq.heappush(heap, (intervals[n][pos+1].start, intervals[n][pos+1].end, n, pos+1))

        result.append(Interval(start, end))
        return result

if __name__ == "__main__":
    sln = Solution()

    input = [
                [Interval(1,3), Interval(4,7), Interval(6,8)],
                [Interval(1,2), Interval(9,10)]
            ]
    res = sln.mergeKSortedIntervalLists(input)
    print(res)