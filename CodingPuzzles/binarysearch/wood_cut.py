def woodcut(l, k):
    print("aa")

def test_0():
    print("Test 0")

    wood_lengths = [232, 124, 456]
    k = 7
    ans = 114

    res = woodcut(wood_lengths, k)

    if ans == res:
        print("PASS - result: {0}, expected {1}".format(res, ans))
    else:
        print("FAIL - result: {0}, expected {1}".format(res, ans))

if __name__ == '__main__':
    test_0()