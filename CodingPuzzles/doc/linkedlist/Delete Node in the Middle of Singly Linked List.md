# Problem

http://www.lintcode.com/en/problem/delete-node-in-the-middle-of-singly-linked-list/

Implement an algorithm to delete in a node in the middle of a singly linked list, given only access to that node.

** Example **

Given ```1->2->3->4``` and node ```3```, return ```1->2->4```

# Thoughts

- Only has access to the given node, so removing the node can be done by changing the node to the node's next

# My Solution

```
    def deleteNode(self, node):
        # write your code here
        if node is None or node.next is None:
            return
        
        next = node.next
        node.val = next.val
        node.next = next.next
        return

```

# Reference