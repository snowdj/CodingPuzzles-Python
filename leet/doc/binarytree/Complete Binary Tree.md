# Complete Binary Tree

## Problem

Check a binary tree is completed or not. A complete binary tree is a binary tree that every level is completed filled except the deepest level. In the deepest level, all nodes must be as left as possible.

**Example**

```
    1
   / \
  2  3
 /
4  
```

is a complete binary tree.

```
    1
   / \
  2  3
  \
   4
```

is not a complete binary tree.


## Thoughts

- Recursive method is hard to implement to resolve this problem
    - The deepest level's upper level can have both left and right, or only left
- Represent the binary tree as an array
    - A complete binary tree have no None node in between, all the None node only stays in the last

## My Solution

```python
def isComplete(self, root):
    # Write your code here
    if root is None
        return True
    queue = [root]
    index = 0
    while index < len(queue):
        if queue[index] is not None:
            queue.append(queue[index].left)
            queue.append(queue[index].right)
        index += 1

    while queue[-1] is None:
        queue.pop()

    for q in queue:
        if q is None:
            return False
    return True
```

## Reference
