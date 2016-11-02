# Problem

http://www.lintcode.com/en/problem/remove-node-in-binary-search-tree/

Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

# Thoughts

- The difficulty is after removing the node, need move other nodes in order to keep the tree be a BST - a reconstructing process
- One way to solve this problem is using 2 steps
  - Remove the node
  - Rebuild the BST tree with other nodes
- Record all the nodes: In-order traversal
- Rebuild the BST tree: Use the In-order nature, recursively build the tree

# My Solution

```
    ans = []
    
    def inorder(self, root, value):
        if root is None:
            return
    
        self.inorder(root.left, value)
        
        if root.val != value:
            self.ans.append(root.val)
        
        self.inorder(root.right, value)
    
    def buildtree(self, l, r):
        if l == r:
            node = TreeNode(self.ans[l])
            return node
        
        if l > r:
            return None
        
        mid = (l+r) / 2
        node = TreeNode(self.ans[mid])
        node.left = self.buildtree(l, mid - 1)
        node.right = self.buildtree(mid+1, r)
        
        return node
        
    def removeNode(self, root, value):
        # write your code here
        self.inorder(root, value)
        return self.buildtree(0, len(self.ans)-1)
        
```

# Reference
