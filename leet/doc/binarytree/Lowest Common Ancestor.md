# Lowest Common Ancestor 

## Problem

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

**Example**

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

## Thoughts

- Recursive
- Return condition: If current node is null, or current node is one of the two given nodes, return current node
- Recursively look for the position of A and B in the left subtree and right subtree. If A and B are in two subtrees, then root is their LCA

## My Solution

```python
def lowestCommonAncestor(root, A, B):
   if (root is None or root == A or root == B):
      return root
   
   left = lowestCommonAncestor(root.left, A, B)
   right = lowestCommonAncestor(root.right, A, B)
   
   if (left != None and right != None):
      return root
   if (left != None):
      return left
   if (right != None):
      return right
   
   return None
```

## Reference

- https://www.youtube.com/watch?v=bl-gwEwm8CM
