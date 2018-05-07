class Solution:
    def searchBigSortedArray_0(self, reader, target):
        # write your code here
        UNEXIST = 2, 147, 483, 647
        INIT_END = 1

        last_end = INIT_END
        while (reader.get(last_end) != UNEXIST):
            if last_end == INIT_END:
                start = 0
            else:
                start = last_end + 1
            end = last_end * 2
            last_end = end
            while (start + 1 < end):
                mid = start + (end - start) // 2
                midval = reader.get(mid)
                if midval == UNEXIST:
                    return -1
                if target <= midval:
                    end = mid
                else:
                    start = mid
            if reader.get(start) == target:
                return start
            if reader.get(end) == target:
                return end

        return -1

    def searchBigSortedArray(self, reader, target):
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1

        start, end = 0, index
        while start + 1 < end:
            mid = start + (end - start)//2
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1

if __name__ == "__main__":
    solution = Solution()

    test_input = [1,3,6,9,21]
    result = solution.searchBigSortedArray(test_input, 4)
    expected_res = 4
    print(result)
    assert(result == expected_res)

