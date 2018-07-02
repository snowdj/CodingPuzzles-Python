class Solution():
    def kClosestNumbers(A, target, k):
        if A is None or len(A) == 0 or target is None or k is None or k == 0:
            return []

        start, end = 0, len(A) - 1
        closest = 0
        while (start + 1 < end):
            mid = start + (end - start)//2
            if target == A[mid]:
                closest = mid
                break
            elif target < A[mid]:
                end = mid
            else:
                start = mid

        if closest != mid:
            if abs(A[start] - target) <= abs(A[end] - target):
                closest = start
            else:
                closest = end

        return findK(A, target, k, closest)

class Solution1():
    def findK(A, target, k, closest_pos):
        k_nums = [A[closest_pos]]
        left, right = closest_pos - 1, closest_pos + 1
        while k - 1 > 0:
            if left >= 0 and right <= len(A) - 1:
                if abs(A[left] - target) <= abs(A[right] - target):
                    k_nums.append(A[left])
                    left -= 1
                else:
                    k_nums.append(A[right])
                    right += 1
            elif left >= 0:
                k_nums.append(A[left])
                left -= 1
            else:
                k_nums.append(A[right])
                right += 1
            k -= 1
        return k_nums

class Solution2():
    """
    Remove the len(arr) - k farthest numbers
    """
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr is None or len(arr) == 0 or k is None or k == 0 or x is None:
            return []

        if len(arr) == 1:
            return arr

        while len(arr) > k:
            if abs(arr[0] - x) > abs(arr[-1] - x):
                arr.pop(0)
            else:
                arr.pop(-1)

        return arr

class Solution3():
    def kClosestNumbers_2(A, target, k):
        dic = {i: abs(i - target) for i in A}
        res = [j for j in sorted(dic, key=dic.get)]
        return res[:k]


class Solution4():
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr is None or len(arr) == 0 or k is None or k == 0 or x is None:
            return []

        # find the number closest to x
        idx = self.find_closest_index(arr, x)
        return self.find_k(arr, k, x, idx)

    def find_closest_index(self, arr, x):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] > x:
                end = mid
            else:
                start = mid

        if abs(arr[start] - x) <= abs(arr[end] - x):
            return start
        return end

    def find_k(self, arr, k, x, pivot_idx):
        found = [arr[pivot_idx]]
        left, right = pivot_idx - 1, pivot_idx + 1
        while len(found) < k and (left >= 0 or right <= len(arr) - 1):
            if left >= 0 and right <= len(arr) - 1:
                if abs(arr[left] - x) > abs(arr[right] - x):
                    found.append(arr[right])
                    right += 1
                else:
                    found.append(arr[left])
                    left -= 1
            elif left >= 0:
                found.append(arr[left])
                left -= 1
            elif right <= len(arr) - 1:
                found.append(arr[right])
                right += 1

        return sorted(found)

if __name__ == "__main__":
    sln = Solution4()
    res = sln.findClosestElements([1,2,3,4,5], 4, 3)
    print(res)
    expected_result = [1,2,3,4]

    res = sln.findClosestElements([1,4,6,8], 3, 3)
    print(res)
    expected_result = [4,1,6]

    res = sln.findClosestElements([1,4,6,10,20], 21, 4)
    print(res)
    expected_result = [20,10,6,4]

