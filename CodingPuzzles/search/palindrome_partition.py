result = []

def isPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) -1 -i]:
            return False
    return True

def dfs_visit(s, stringlist):
    global result

    if len(s) == 0:
        print "stringlist: ", stringlist
        result.append(stringlist)

    for i in range(1, len(s) + 1): # when i == len(s), s[i:] is empty string, which will cause result be updated
        if isPalindrome(s[:i]):
           dfs_visit(s[i:], stringlist + [s[:i]])

def partition(s):
    global result
    dfs_visit(s, [])
    print result

def test():
    s = 'aab'
    print "Test Data: "
    print s

    print "Test Result: "
    partition(s)

if __name__ == "__main__":
    test()