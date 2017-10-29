# Problem

http://www.lintcode.com/en/problem/rotate-list/

Given a list, rotate the list to the right by ```k``` places, where k is non-negative.

**Example**

Given ```1->2->3->4->5``` and k = ```2```, return ```4->5->1->2->3```

# Thoughts

- Find the length of linked list, k%L is the number of positions that the elements need rotate right

# My Solution

```python
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return None
            
        if k == 0:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next # connect the last node to the head node
        step = count - ( k % count )
        for i in range(0, step):
            p = p.next
        head = p.next
        p.next = None
        return head
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3785465.html

