# Balance Binary Tree

## Problem

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

**Example**

Given binary tree A = ```{3,9,20,#,#,15,7}```, B = ```{3,#,20,15,7}```

```
A)  3                  B)  3
   / \                      \
  9  20                     20
    /  \                    / \
   15   7                  15  7
```

The binary tree A is a height-balanced binary tree, but B is not.

## Thoughts

- Recursively traverse the tree. Get the height difference of each node. 
- Divide and conquer
- First, work on the left sub-tree. Then work on the right sub-tree
- Condition of balanced: abs(leftHeight - rightHeight) <= 1
- Height: max(leftHeight, rightHeight) + 1 # 1 is the depth of current node

## My Solution

```python
def isBalanced(root):
  balanced, height = validate(root)
  return balanced
  
def validate(root):
  if root is None:
    return True, 0  # exit condition, one node, isBalanced is True
  
  balanced, leftHeight = validate(root.left)
  if not balanced:
    return False, 0
  
  balanced, rightHeight = validate(root.right)
  if not balanced:
    return False, 0
  
  return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1
```

## Reference
