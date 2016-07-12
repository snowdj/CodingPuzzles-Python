# Problem

http://www.lintcode.com/en/problem/search-range-in-binary-search-tree/

Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in range k1 to k2. ie. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending order.

** Example **

If k1 = ```10``` and k2 = ```22```, then your function should return ```[12,20,22]```

```
   20
   /\
  8 22
 / \
4  12
  
```

# Thoughts

- Use DFS, or use a queue and while loop
- Sort the final result
- How to improve: if a node.val < min(k1, k2), then no need to check node.left

# My Solution

```
    def searchRange(self, root, k1, k2):
        # write your code here
        
        ans = []
        self.dfs(root, k1, k2, ans)
        
        return sorted(ans)
    
    def dfs(self, node, k1, k2, ans):
        if node is None:
            return
        
        if node.val >= k1 and node.val <= k2:
            ans.append(node.val)
        
        if node.left:
            self.dfs(node.left, k1, k2, ans)
        if node.right:
            self.dfs(node.right, k1, k2, ans)
```


```
def searchRange(self, root, k1, k2):
    ans = []
    if root is None:
        return ans
    
    queue = [root]
    index = 0
    while index < len(queue):
        if queue[index] is not None:
            if queue[index].val >= k1 and \
                queue[index].val <= k2:
                    ans.append(queue[index].val)
            
            queue.append(queue[index].left)        
            queue.append(queue[index].right)
        index += 1
    
    return sorted(ans)
```

# Reference
