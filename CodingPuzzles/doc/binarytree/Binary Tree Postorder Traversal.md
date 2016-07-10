# Problem

http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/

Given a binary tree, return the postorder traversal of its nodes' values.

Given binary tree ```{1,#,2,3}```

```
   1
    \
     2
    /
   3  
```

Return ```[3,2,1]```

# Thoughts

- Recursive, Divide and Conquer
- left, right, root

# My Solution

```
    def postorderTraversal(self, root):
        # write your code here

        if root is None:
            return []
        
        postorder = []
        self.rec(root, postorder)
        
        return postorder
    
    def rec(self, node, order):
        if node is None:
            return
        
        if node.left:
            self.rec(node.left, order)
        if node.right:
            self.rec(node.right, order)
        order.append(node.val)
```

# Reference
