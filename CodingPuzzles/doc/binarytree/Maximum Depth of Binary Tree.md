# Maximum Depth of Binary Tree

## Problem

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example**

Given a binary tree as follow:

```
  1
 / \
2   3
   / \
  4   5
```

The maximum depth is ```3```.

## Thoughts

Use divide-and-conquer + recursive algorithm to solve this problem.

## My Solution

```
def maxDepth(root):
  if root is None:
    return 0
  
  return max(maxDepth(root.left), maxDepth(root.right)) + 1
```
