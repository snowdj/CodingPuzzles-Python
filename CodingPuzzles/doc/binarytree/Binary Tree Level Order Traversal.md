# Problem

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level). 
 
**Example**

```
    3
   / \
  9  20
    /  \
   15  7
```

return is level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

# Thoughts

- BFS
- Result is a list of list, each sublist stores the nodes of one level
- If the level doesn't exist, add a sublist: ```result.append([])```
- Use pre-order traversal to visit each node, and append them to levels accordingly
- Why use preorder: starting from root first

# My Solution

```
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: 
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
            
    def levelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        return res
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3722081.html
