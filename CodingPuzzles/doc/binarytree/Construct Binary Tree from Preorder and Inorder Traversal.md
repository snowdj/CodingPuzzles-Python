# Problem

http://www.lintcode.com/en/problem/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

- You may assume that duplicates do not exist in the tree.

**Example**

Given in-order ```[1,2,3]``` and pre-order ```[2,1,3]```, return a tree:

```
  2
 / \ 
1  3
```

# Thoughts

- Recursive
- Pre-order: first element is root
- In-order: from 1st element to where the root element is - left tree in-order; from root element to the right - right tree in-order. The number of left tree nodes are the same number as in pre-order tree
- left tree:
  - pre-order: elements in the range of  [0, index)
  - in-order: elements in the range of [1, index+1): element 1 is root
- right tree:
  - pre-order: elements in the range of [index+1, end]
  - in-order: elements in the range of [index+1, end]
- Corner condition

```
input : preorder = [], inorder = [] 
```

# My Solution

```
    def buildTree(self, preorder, inorder):
        # write your code here
        
        if preorder is None or inorder is None:
            return None
        
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:rootPos+1], inorder[0:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:], inorder[rootPos+1:])
        
        return root

```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3720138.html

