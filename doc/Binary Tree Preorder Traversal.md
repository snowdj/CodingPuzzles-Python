# Binary Tree Preorder Traversal

## Problem
Given a binary tree, return the preorder traversal of its nodes' values.

**Example**

Given:

```
    1
   / \
  2   3
 / \
4   5
```

return ```[1,2,4,5,3]```

## Thoughts

- Preorder traversal is "Root First Traversal". DLR: The visit sequence is: root -> left -> right.
- Use recursive method or stack to resolve this problem
- Stack method:
	- Build the stack
	- Build the preorder sequence
- About Building the stack
	- Add the right node to stack first, because a stack is a FILO. The left node in the stack will be poped from stack and appended to the preorder sequence first.

## My Solution

```
def preorderTraversal(root):
  if root is None:
    return []
  
  preorder = []
  stack = [root]
  
  while stack:
    node = stack.pop()
    preorder.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
    
    return preorder
end                   
```