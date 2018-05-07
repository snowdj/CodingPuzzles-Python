def strStr(source, target):
    # write your code here
    if source is None or target is None:
        return -1

    if source == target:
        return 0

    if target == "":
        return 0

    l_source = list(source)
    l_target = list(target)
    for i, s in enumerate(l_source):
        match = False
        if l_target[0] == s:
            if i + len(l_target) > len(l_source):
                return -1
            for j, t in enumerate(l_target):
                if t != l_source[i+j]:
                    break
                if j == len(l_target) - 1:
                    match = True

            if match:
                return i

    return -1

if __name__ == "__main__":
    res = strStr("tartarget", "target")
    print(res)