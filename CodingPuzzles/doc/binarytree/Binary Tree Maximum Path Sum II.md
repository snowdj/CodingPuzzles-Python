# Binary Tree Maximum Path Sum II

## Problem 

Given a binary tree, find the maximum path sum from root.
The path may end at any node in the tree and contain at least one node in it.

Example
Given the below binary tree:

```
   1
  / \
 2   3
```
return ```4```. (1->3)

## Thoughts
- The solution need record sums of all paths, so use DFS

## My Solution

```
class Solution:

    def dfs(self, node, length, vals):
        length += node.val
        vals.append(length)
        if node.left is not None:
            self.dfs(node.left, length, vals)
        if node.right is not None:
            self.dfs(node.right, length, vals)
    
    def maxPathSum2(self, root):
        # Write your code here
        if root is None:
            return 0

        vals = []
        self.dfs(root, 0, vals)
        return max(vals)
```