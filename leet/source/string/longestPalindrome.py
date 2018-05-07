def longestPalindrome(s):
    if s is None or len(s) == 0:
        return 0

    # use a hash to count how many times each character appears
    count = count_words(s)
    print(count)

    total = 0
    addone = False
    for c, n in count.items():
        if n // 2 >= 1:
            total += 2 * (n // 2)
        if not addone and (n % 2 == 1 or n == 1):
            total += 1
            addone = True

    return total


def count_words(s):
    from collections import Counter
    return Counter(list(s))


if __name__ == "__main__":
    test_str = "abccccdd"
    expected_result = 7
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "aaaa"
    expected_result = 4
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)

    test_str = "a"
    expected_result = 1
    res = longestPalindrome(test_str)
    print("test_str: {0}, result: {1}".format(test_str, res))
    assert (res == expected_result)