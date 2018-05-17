def sequenceReconstruction(org, seqs):
    from collections import defaultdict
    indegrees = defaultdict(int)
    edges = defaultdict(list)
    for s in seqs:
        if len(s) == 1:
            indegrees[s[0]] = 0
            edges[s[0]] = []
        else:
            for i in range(len(s) - 1):
                if s[i+1] not in edges[s[i]]:
                    indegrees[s[i+1]] += 1
                edges[s[i]].append(s[i+1])

    start = -1
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            start = i
            break

    if start == -1:
        return False

    queue = [start]

    while len(queue) > 0:
        n = queue[0]
        del queue[0]

def sequenceReconstruction_bfs(org, seqs):
    from collections import defaultdict
    edges = defaultdict(list)
    indegrees = defaultdict(int)
    nodes = set()

    # build the graph for seqs
    for seq in seqs:
        nodes |= set(seq)
        for i in range(len(seq)):
            if i == 0:
                indegrees[seq[i]] += 0
            if i < len(seq) - 1:
                edges[seq[i]].append(seq[i+1])
                indegrees[seq[i+1]] += 1

    queue = [k for k in indegrees if indegrees[k] == 0]
    res = []

    while len(queue) == 1:
        cur_node = queue.pop()
        res.append(cur_node)
        for node in edges[cur_node]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                queue.append(node)

    if len(queue) > 1:
        return False
    return len(res) == len(nodes) and res == org

if __name__ == "__main__":
    #org = [1,2,3]
    #seqs = [[1,2]]
    #result = sequenceReconstruction_bfs(org, seqs)
    #print(result)

    org = [1,2,3]
    seqs = [[1,2],[1,3],[2,3]]
    result = sequenceReconstruction_bfs(org, seqs)
    print(result)