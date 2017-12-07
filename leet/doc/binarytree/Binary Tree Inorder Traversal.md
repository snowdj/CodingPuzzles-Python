# Binary Tree Inorder Traversal

## Problem

http://www.lintcode.com/en/problem/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

Given binary tree ```{1,#,2,3}```

```
  1
   \
   2
  /
 3  
```

Return ```[1,3,2]```

# Thoughts

- Recursive + Divide and Conquer
- inorder traversal: left, root, right

# My Solution

```python
def inorderTraversal(self, root):
    # write your code here
    if root is None:
        return []
    
    inorder = []
    self.rec(root, inorder)
    return inorder
    
    def rec(self, node, order):
        if node.left:
            self.rec(node.left, order)
    
        order.append(node.val)
    
        if node.right:
            self.rec(node.right, order)
```

## Reference
