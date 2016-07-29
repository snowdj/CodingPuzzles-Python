# Problem

http://www.lintcode.com/en/problem/insert-node-in-a-binary-search-tree/

Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

* You can assume there is no duplicate values in this tree + node

**Example**

Given binary search tree as follow, after insert node 6, the tree should be:

```
  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6
```

# Thoughts

- Binary Search Tree: left < root, right > root
- Insert Position: can be a replacement
- The assumption is important: assume no duplicate values in this tree + node

# My Solution

```

def insertNode(self, root, node):
    if (root is None):
        root = node
        return root
    
    tmp = root
    last = None
    
    while (tmp != None):
        last = tmp
        if (tmp.val > node.val):
            tmp = tmp.left
        else:
            tmp = tmp.right
    
    if (last != None):
        if (last.val > node.val):
            last.left = node
        else:
            last.right = node
    
    return root
```

# Reference
