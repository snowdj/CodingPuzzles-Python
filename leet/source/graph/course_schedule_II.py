def findOrder(numCourses, prerequisites):
    # write your code here
        if numCourses is None or prerequisites is None:
            return []

        edges = {i:[] for i in range(numCourses)}
        indegrees = [0 for i in range(numCourses)]
        for i, j in prerequisites:
            if j in edges and i in edges[j]:
                pass
            else:
                edges[j].append(i)
                indegrees[i] += 1

        result = []
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            n = queue[0]
            del queue[0]
            result.append(n)
            for e in edges[n]:
                indegrees[e] -= 1
                if indegrees[e] == 0:
                    queue.append(e)

        if len(result) < numCourses:
            return []
        return result


if __name__ == "__main__":
    n = 10
    pre = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
    result = findOrder(n, pre)
    print(result)
