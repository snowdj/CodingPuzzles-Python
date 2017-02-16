# Problem

http://www.lintcode.com/en/problem/topological-sorting/

Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

**Notice**

Graph representation:

```{1,2,4#2,1,4#3,5#4,1,2#5,3}``` represents follow graph:

```
1------2  3
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      4   5
```

we use # to split each node information.
1,2,4 represents that 2, 4 are 1's neighbors
2,1,4 represents that 1, 4 are 2's neighbors
3,5 represents that 5 is 3's neighbor
4,1,2 represents that 1, 2 are 4's neighbors
5,3 represents that 3 is 5's neighbor

# Thoughts

- Use DFS or BFS, both works
- Find the nodes with no incoming edges: These nodes are not neighbors of any other nodes.


# My Solution

## Solution 1

Complexity: O(n^2)

```
def topSort(graph):
    sln = []
    graph = set(graph)
    while len(graph):
        hs = set()
        for node in graph:
            hs.add(node)
        for node in graph:
            for nb in node.neighbors:
                if nb in hs:
                    hs.remove(nb)
        for node in hs:
            graph.remove(node)
            sln.append(node)
    return sln
```

## Solution 2: DFS

Complexity: O(n^2)

```
ans = []
def topSort(graph):
    countrd = {} # count the incoming edges (rudu)
    for x in graph:
        countrd[x] = 0
    for i in graph:
        for j in i.neighbors:
            countrd[j] = countrd[j] + 1
    
    for i in graph:
        if countrd[i] == 0:
            dfs(i, countrd, ans)

def dfs(i, countrd, ans):
    ans.append(i)
    countrd[i] -= 1
    for j in i.neighbors:
        countrd[j] = countrd[j] - 1
        if countrd[j] == 0:
            dfs(j, countrd, ans)
    
```

# Reference

- http://shengshuyang.github.io/topological-sorting.html

