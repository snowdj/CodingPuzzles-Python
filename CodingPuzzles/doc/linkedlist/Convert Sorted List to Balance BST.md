# Problem

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

**Example**

```
1->2->3 =>    2
             / \
            1  3
```

# Thoughts

- Save the values of nodes in linked list in an array
- The element in the middle of the array (len/2) is the root node
- Recursively build the BST

# My Solution

```
    def sortedListToBST(self, head):
        # write your code here
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return self.sortedArrayToBST(array)
    
    def sortedArrayToBST(self, array):
        length = len(array)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(array[0])
        
        root = TreeNode(array[length/2])
        root.left = self.sortedArrayToBST(array[:length/2])
        root.right = self.sortedArrayToBST(array[length/2+1:])
        return root
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3722114.html

