def subsets(S):
    def dfs(depth, start, valuelist):
        print("depth={0}, start={1}, valuelist={2}".format(depth, start, valuelist))
        if len(valuelist) > 0:
            res.append(valuelist)

        if depth == len(S):
            print("time to return")
            return
        for i in range(start, len(S)):
            dfs(depth+1, i+1, valuelist+[S[i]])

    S.sort()
    res = []
    dfs(0, 0, [])
    return res

def test_run():
    print(subsets([1,2,3]))
    #print(subsets([3,2,1]))

if __name__ == "__main__":
    test_run()