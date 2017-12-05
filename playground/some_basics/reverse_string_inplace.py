# Given a string, reverse it in-place, without the "reverse" function
# eg.
# abcde => edcba
# jazz => zzaj
#
# solution: use two pointers, swap the character they point to, then move pointers until they meet

def reverse_str(input_str):
    if input_str is None or len(input_str) <= 1:
        return input_str

    begin = 0
    end = len(input_str) - 1
    input = list(input_str)
    while (begin < end):
        #print("begin: {0}, end: {1}".format(begin, end))
        t = input[begin]
        input[begin] = input[end]
        input[end]= t
        begin += 1
        end -= 1

    return ''.join(input)

if __name__ == "__main__":
    test_str = "abcde"
    print(reverse_str(test_str))
    assert(reverse_str(test_str) == test_str[::-1])

    test_str = "jazz"
    print(reverse_str(test_str))
    assert(reverse_str(test_str) == test_str[::-1])

    test_str = "alab11134"
    print(reverse_str(test_str))
    assert(reverse_str(test_str) == test_str[::-1])

