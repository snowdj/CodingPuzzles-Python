def intersect(arr1, arr2):

    if len(arr1) == 0 or len(arr2) == 0:
        return []

    intarr = []

    for i in range(len(arr1)):
        # print "check element: ", arr1[i]
        if arr1[i] in arr2:
            if not arr1[i] in intarr:
                intarr.append(arr1[i])

    return intarr

def intersect2(arr1, arr2):

    if len(arr1) == 0 or len(arr2) == 0:
        return []

    a = set(arr1)
    b = set(arr2)
    c = a.intersection(b)

    return list(c)

def test():
    input_array_1 = [-3, 1, 2, -3, 4];
    input_array_2 = [1,-3]
    print "Test Data: "
    print input_array_1
    print input_array_2

    print "Test Result -- intersect: "
    print intersect(input_array_1, input_array_2)

    print "Test Result -- intersect2: "
    print intersect2(input_array_1, input_array_2)

if __name__ == "__main__":
    test()