# Problem

http://www.lintcode.com/en/problem/lowest-common-ancestor-ii/

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor (LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
The node has an extra attribute ```parent``` which point to the father of itself. The root's parent is null.

Example
For the following binary tree:

```
   4
  / \
 3   7
    / \
   5   6
```

LCA(3,5) = 4
LCA(5,6) = 7
LCA(6,7) = 7

# Thoughts

- Similar to Lowest Common Ancestor where the node doesn't have a parent pointer, but easier
- Since the parent pointer exists, we can find the paths from the root to the given node, and find out the LCA
- LCA is the last element where the nodes' paths diverge
- Summary
  - Find the path from root node to the target nodes
  - Find the node where the two paths start to diverge

# My Solution

```
    def lowestCommonAncestorII(self, root, A, B):
        # Write your code here
        path1 = self.path_from_root(A)
        path2 = self.path_from_root(B)
        lca = None
        for n1, n2 in zip(path1, path2):
            if n1 != n2:
                return lca
            lca = n1
        return lca

    def path_from_root(self, node):
        path = []
        while node:
            path.insert(0, node)
            node = node.parent
        return path
```

# Reference

- https://www.youtube.com/watch?v=bl-gwEwm8CM