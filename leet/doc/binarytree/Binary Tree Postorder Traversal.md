# Binary Tree Postorder Traversal

## Problem

http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.

**Example**

Given binary tree ```{1,#,2,3}```

```
   1
    \
     2
    /
   3  
```

Return ```[3,2,1]```

## Thoughts

- Recursive, Divide and Conquer
- Postorder: left, right, root

## My Solution

```Python
def postorderTraversal(root):
    # write your code here
    if root is None:
        return []
        
    postorder = []
    rec(root, postorder)
        
    return postorder
    
def rec(node, order):
    if node is None:
        return
        
    if node.left:
        self.rec(node.left, order)
    if node.right:
        self.rec(node.right, order)
    order.append(node.val)
```

## Reference
