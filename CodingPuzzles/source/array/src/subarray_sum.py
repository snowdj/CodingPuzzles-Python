def subarraySum(nums):

    for i in range(len(nums)):
        if nums[i] == 0:
            return [i, i]

        sum = nums[i]

        for j in range(i+1, len(nums)):
            sum += nums[j]
            if sum == 0:
                return [i, j]

    return []


def test():
    input_array = [-3, 1, 2, -3, 4];
    print "Test Data: "
    print input_array

    print "Test Result: "
    print subarraySum(input_array)

if __name__ == "__main__":
    test()