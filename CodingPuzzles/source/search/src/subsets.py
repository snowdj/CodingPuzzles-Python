def subsets(S):
    def dfs(depth, start, valuelist):
        cnt[0] += 1
        print("---- calling DFS #{0}".format(cnt[0]))
        print("depth: {0}".format(depth))
        print("start: {0}".format(start))
        print("valuelist: {0}".format(valuelist))

        res.append(valuelist)
        if depth == len(S):
            print("time to return")
            return
        for i in range(start, len(S)):
            print("i = {0}".format(i))
            print("S[i]: {0}".format(S[i]))
            dfs(depth+1, i+1, valuelist+[S[i]])

    S.sort()
    res = []
    cnt = [0]
    dfs(0, 0, [])
    return res

def test_run():
    print(subsets([1,2,3]))
    #print(subsets([3,2,1]))

if __name__ == "__main__":
    test_run()