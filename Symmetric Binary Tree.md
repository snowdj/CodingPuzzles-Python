# Problem

http://www.lintcode.com/en/problem/symmetric-binary-tree/

Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Thoughts

- Note the comparision happen on the node's left tree, and the node's right tree

# My Solution

```
    def help(self, a, b):
        if a == None and b == None:
            return True
        
        if a and b and a.val == b.val:
            if self.help(a.right, b.left) and self.help(a.left, b.right):
                return True
        
        return False
    
    def isSymmetric(self, root):
        # Write your code here
        if root:
            return self.help(root.left, root.right)
        return True
```

# Reference

