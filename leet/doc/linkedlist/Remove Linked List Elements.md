# Problem

http://www.lintcode.com/en/problem/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value ```val```. 

**Example**

Given ```1->2->3->3->4->5->3```, val = 3, you should return the list as ```1->2->4->5```

# Thoughts

- Use a dummy node, because original head node can be deleted
- If using method 1, pay attention to when to update the lastHead

# My Solution

## Method 1
```python
    def removeElements(self, head, val):
        # Write your code here
        if head is None or val is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        lastHead = dummy
        while head:
            if head.val == val:
               lastHead.next = head.next
            else:
                lastHead = head
            head = head.next
        
        return dummy.next
```

## Method 2
```python
    def removeElements(self, head, val):
        if head is None or val is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        newHead = dummy
        while (dummy and dummy.next):
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        return newHead.next

```

# Reference