def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def dfs(s, stringlist):
    print("** s ** {0}".format(s))
    if len(s) == 0:
        print("updating res, add {0}".format(stringlist))
        res.append(stringlist)
    for i in range(1, len(s) + 1):
        print("checking {0}".format(s[:i]))
        print("i = {0}".format(i))
        if isPalindrome(s[:i]):
            print("yes -- update stringlist: {0}".format(stringlist + [s[:i]]))
            dfs(s[i:], stringlist + [s[:i]])

def partition(s):
    return dfs(s, [])

if __name__ == '__main__':
    res = []
    partition("aab")
    print(res)

    #del res[:]
    #partition("abbac")
    #print(res)