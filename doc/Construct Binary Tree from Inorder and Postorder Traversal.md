# Problem

http://www.lintcode.com/en/problem/construct-binary-tree-from-inorder-and-postorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

- You may assume that duplicates do not exist in the tree.

# Thoughts

- Similar to "Construct Binary Tree from Preorder and Inorder Traversal"
- Last element of post order is the root
- Find the position of root in inorder traversal
- Recursive

# My Solution

```
    def buildTree(self, inorder, postorder):
        # write your code here
        if inorder is None or postorder is None:
            return None
        
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[0:rootPos], postorder[0:rootPos])
        root.right = self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1])
        
        return root
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3720138.html

