# Problem

http://www.lintcode.com/en/problem/merge-two-sorted-lists/

Merge two sorted (ascending) linked lists and return it as a new sorted list. The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.

** Example **

Given ```1->3->8->11->15->null```, ```2->null```, return ```1->2->3->8->11->15->null```. 

# Thoughts

- Merge sort
- Use a dummy node

# My Solution

```
    def mergeTwoLists(l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        ph1 = l1
        ph2 = l2
        dummy = ListNode(0)
        dhead = dummy
        
        while ph1 and ph2:
            if ph1.val < ph2.val:
                dummy.next = ph1
                ph1 = ph1.next
            else:
                dummy.next = ph2
                ph2 = ph2.next
            dummy = dummy.next
        
        if ph1:
            dummy.next = ph1
        if ph2:
            dummy.next = ph2
        
        return dhead.next
```

# Reference

