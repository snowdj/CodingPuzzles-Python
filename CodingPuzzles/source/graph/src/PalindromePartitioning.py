def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def dfs(s, stringlist):
    if len(s) == 0:
        res.append(stringlist)
    for i in range(1, len(s) + 1):
        if isPalindrome(s[:i]):
            dfs(s[i:], stringlist + [s[:i]])

def partition(s):
    return dfs(s, [])

if __name__ == '__main__':
    res = []
    partition("aab")
    print(res)

    del res[:]
    partition("abbac")
    print(res)