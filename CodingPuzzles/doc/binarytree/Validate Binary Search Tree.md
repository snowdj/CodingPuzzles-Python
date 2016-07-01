# Problem

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
- A signle node tree is a BST.

Example
```
  2
 / \
1  4
  / \
 3   5
```
The above binary tree is serialized as {2,1,4,#,#,3,5}

# Thoughts

- Use recursive algorithm to resolve this problem
- All left subtree nodes values are in the range of [MIN, current node value)
- All right subtree nodes values are in the range of (current node value, MAX]
- In Python, MIN is: float("-infinity"); MAX is float("infinity")

# My Solution

```
class Solution:
    # @param root, a tree node
    # @return a boolean
    def ValidBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
    
    def isValidBST(self, root):
        return self.ValidBST(root, float("-infinity"), float("infinity"))
```

# Reference
[4 Methods](http://www.cnblogs.com/yuzhangcmu/p/4177047.html)
