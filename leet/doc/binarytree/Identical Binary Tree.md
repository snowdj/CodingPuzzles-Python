# Identical Binary Tree

## Problem

http://www.lintcode.com/en/problem/identical-binary-tree/

Check if two binary trees are identical. Identical means the two binary trees have the same structure and every identical position has the same value.

## Thoughts

- Recursive
- When both nodes exist and the values are the same, comopare them
    - nodeA.left == nodeB.left && nodeA.right == nodeB.right

## My Solution

```python
def isIdentical(self, a, b):        
    if a is None and b is None:
        return True
        
    if a and b and a.val == b.val:
        if self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right):
            return True
        
    return False
```

## Reference
