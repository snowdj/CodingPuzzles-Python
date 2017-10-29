# Problem

http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list-ii

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

**Example**

Given ```1->2->3->3->4->4->5```, return ```1->2->5```. 
Given ```1->1->1->2->3```, return ```2->3```. 

# Thoughts

- It's impossible that the duplicated elements are not consecutive in the list, because the given list is a *sorted* linked list
- Note this problem requires to remove ALL duplicated nodes, not keeping only one
- New list's end element's next pointer must point to None
- As all duplicated nodes need be removed, need add a dummy node to the head to handle removing the original head node
- When two nodes having the same value are found, use a another while loop to skip all the duplicated nodes (move the head.next pointer). If not doing it this way, the last repetition node might NOT be removed, such as ```dummy->1->1->1->2```

# My Problem

```python
def deleteDuplicates(head):
    if head is None or head.next is None:
        return head
    
    dummy = ListNode(head.val, head)
    head = dummy
    
    while head.next and head.next.next:
        if head.next.val == head.next.next.val:
            val = head.next.val
            while head.next is not None and head.next.val == val:
                head.next = head.next.next
        else:        
            head = head.next
    
    return dummy.next
```

# Reference

