# Problem

http://www.lintcode.com/en/problem/clone-graph/

Clone an undirected graph. Each node in the graph contains a ```label``` and a list of its ```neighbors```.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use ```#``` as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph ```{0,1,2#1,2#2,2}```.

The graph has a total of three nodes, and therefore contains three parts as separated by ```#```.

First node is labeled as ```0```. Connect node ```0``` to both nodes ```1``` and ```2```.
Second node is labeled as ```1```. Connect node ```1``` to node ```2```.
Third node is labeled as ```2```. Connect node ```2``` to node ```2``` (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

```
   1
  / \
 /   \
0 --- 2
     / \
     \_/
```

# Thoughts

- DFS (typical problem)
  - for neighbor in input.neighbors
- Record the visited nodes

# My Solution

```
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

record = {}

def cloneGraph(node):
    def dfs(input, map):
        if input in map:
            return map[input]
        output = UndirectedGraphNode(input.label)
        map[input] = output
        for neighbor in input.neighbors:
            output.neighbors.append(dfs(neighbor, map))
        return output
    
    if node == None:
        return None
    return dfs(node, record)
```

# Reference

