def canFinish(numCourses, prerequisites):
    # write your code here
    if numCourses is None or prerequisites is None:
        return False

    edges = {i: [] for i in range(numCourses)}
    degrees = [0 for i in range(numCourses)]
    for i, j in prerequisites:
        edges[j].append(i)
        degrees[i] += 1

    import Queue
    queue = Queue.Queue(maxsize = numCourses)
    count = 0

    for i in range(numCourses):
        if degrees[i] == 0:
            queue.put(i)

    while not queue.empty():
        node = queue.get()
        print("pop node - {0}".format(node))
        print("queue - {0}".format(queue))
        count += 1

        for x in edges[node]:
            degrees[x] -= 1
            if degrees[x] == 0:
                queue.put(x)

    print("count = {0}".format(count))
    return count == numCourses

def canFinish_1(numCourses, prerequisites):
    if numCourses is None or prerequisites is None:
        return False

    edges = {i:[] for i in range(numCourses)}
    indegrees = [0 for i in range(numCourses)]
    for i, j in prerequisites:
        edges[j].append(i)
        indegrees[i] += 1

    queue = []
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)

    count = 0
    while len(queue) > 0:
        n = queue[0]
        del queue[0]
        count += 1
        for e in edges[n]:
            indegrees[e] -= 1
            if indegrees[e] == 0:
                queue.append(e)

    print("count = {0}".format(count))
    print(numCourses)

    return numCourses == count


if __name__ == "__main__":
    n = 2
    pre = [[1,0]]
    #n = 5
    #pre = [[0,1], [1,2], [2,3], [2,4]]
    result = canFinish_1(n, pre)
    print("result: {0}".format(result))
