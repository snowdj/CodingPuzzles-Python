# Problem

http://www.lintcode.com/en/problem/middle-of-linked-list/

Find the middle node of a linked list.

**Example**

Given ```1->2->3```, return the node with value 2.
Given ```1->2```, return the node with value 1.

# Thoughts

- Use a fast and a slow pointer. Slow pointer reaches the middle when fast pointer reaches the end of the list.
- If there are two nodes, return the first node. This requirement means the condition of while loop is on fast.next.next

# My Solution

```
    def middleNode(self, head):
        # Write your code here
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

# Thoughts

