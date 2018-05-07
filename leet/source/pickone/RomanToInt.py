
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    if s is None:
        return None

    s2v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result_int = 0
    state = 0 # 0-START, 1-CHECK, 2-SPECIAL
    last_i = None
    for i in s:
        if state == 0:
            if i in ['I', 'X', 'C']:
                state = 1
                last_i = i
                continue
            else:
                last_i = i
                result_int += s2v.get(i, 0)
        elif state == 1:
            if last_i is 'I' and i in ['V', 'X']:
                state = 2
            elif last_i is 'X' and i in ['L', 'C']:
                state = 2
            elif last_i is 'C' and i in ['D', 'M']:
                state = 2
            else:
                # calculate the result
                result_int += s2v.get(last_i, 0) + s2v.get(i, 0)
                state = 0
            last_i = i
        elif state == 2:
            result_int += s2v.get(i, 0) - s2v.get(last_i, 0)
            state = 0
            last_i = i

    return result_int


if __name__ == "__main__":
    #test_s = "DCXXI"
    test_s = "MCMXCVI"
    res = romanToInt(test_s)
    print(res)