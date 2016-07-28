# Problem

Find the nth to last element of a singly linked list.
The minimum number of nodes in list in n.

** Example **

Given a list ```3->2->1->5->null``` and n = 2, return node whose value is ```1```. 

# Thoughts

- Use fast and slow pointers
- Move the fast pointer to nth element, then move the faster pointer together with the slow pointer until faster pointer points to null.
- The position that slow pointer at, is the nth to last element

# My Solution

```
    def nthToLast(head, n):
        # write your code here
        if head is None:
            return head
        
        fast = head
        slow = head
        for i in range(0, n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        return slow
```

# Reference

