# Problem

http://www.lintcode.com/en/problem/binary-tree-zigzag-level-order-traversal/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie. from left to right, then right to left for the next level and alternate between). 
 
 **Example**
 
Given binary tree ```{3,9,20,#,#,15,7}```

```
   3
  / \
 9  20
   /  \
  15  7 
```

return its zigzag level order traversal as:

```
[
    [3],
    [20,9],
    [15,7]
]
```

# Thoughts

- BFS
- Result is a list of list, each sublist stores the nodes of one level
- If the level doesn't exist, add a sublist: ```result.append([])```
- Reverse the order of nodes in lines of odd number
- Why use preorder: starting from root first

# My Solution

```
    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
        
        if root.left:
            self.preorder(root.left, level+1, res)
        if root.right:
            self.preorder(root.right, level+1, res)
        
    def zigzagLevelOrder(self, root):
        # write your code here

        if root is None:
            return []
            
        res = []
        self.preorder(root, 0, res)
        return res
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3722022.html

