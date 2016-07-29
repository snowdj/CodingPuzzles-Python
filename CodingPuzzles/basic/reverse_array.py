def reverse_array(list):
    if list is None or len(list) <= 1:
        return list

    for i in range(0, len(list)/2):
        j = len(list) - i - 1
        print(j)
        tmp = list[i]
        list[i] = list[j]
        list[j] = tmp

    return list

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6]
    result = reverse_array(test_list)
    print result

    test_list = [1,2,3,4,5]
    print(reverse_array(test_list))

    test_list = [1,2]
    print(reverse_array(test_list))