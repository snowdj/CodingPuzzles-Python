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


if __name__ == "__main__":
    # res = kClosestNumbers([1,2,3], 2, 3)
    # print(res)
    # expected_result = [2,1,3]
    #
    # res = kClosestNumbers([1,4,6,8], 3, 3)
    # print(res)
    # expected_result = [4,1,6]

    res = kClosestNumbers([1,4,6,10,20], 21, 4)
    print(res)
    expected_result = [20,10,6,4]

