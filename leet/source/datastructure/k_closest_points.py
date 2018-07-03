class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        if points is None or len(points) == 0 or origin is None or k is None or k == 0:
            return []

        import heapq
        heap = []
        for p in points:
            heapq.heappush(heap, (self.dist(p, origin), p.x, p.y))

        result = []
        for i in range(k):
            try:
                pvalue = heapq.heappop(heap)
                result.append([pvalue[1], pvalue[2]])
            except IndexError:
                break

        return result

    def dist(self, point, origin):
        return pow((point.x - origin.x), 2) + pow((point.y - origin.y), 2)