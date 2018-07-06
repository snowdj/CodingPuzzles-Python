class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if arrays is None or arrays == [] or arrays == [[]]:
            return []

        import heapq
        heap = []
        result = []
        for i, arr in enumerate(arrays):
            if len(arr) == 0:
                continue
            heapq.heappush(heap, (arr[0], i, 0))

        while len(heap) > 0:
            val, n, pos = heapq.heappop(heap)
            result.append(val)
            # curr_arr = arrays[n]
            # if pos < len(curr_arr) - 1:
            #     heapq.heappush(heap, (curr_arr[pos+1], n, pos+1))
            if pos < len(arrays[n]) - 1:
                heapq.heappush(heap, (arrays[n][pos+1], n, pos+1))

        return result

if __name__ == "__main__":
    sln = Solution()
    arrays = [
                [1, 3, 5, 7],
                [2, 4, 6],
                [0, 8, 9, 10, 11]
             ]
    res = sln.mergekSortedArrays(arrays)
    print(res)