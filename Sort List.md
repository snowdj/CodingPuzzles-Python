# Problem

http://www.lintcode.com/en/problem/sort-list/

Sort a linked list in O(nlogn) time using constant space complexity.

**Example**

Given ```1->3->2->null```, sort it to ```1->2->3->null```. 

# Thoughts

- Merge sort
- Find the middle of linked list using fast and slow pointers

# My Solution

````
def sortList(head):
    if head is None or head.next is None:
        return head
    
    mid = findMiddle(head)
    right = sortList(mid.next)
    mid.next = None
    left = sortList(head)
    
    return merge(left, right)

def findMiddle(head):
    if head is None or head.next is None:
        return head
    
    pfast = head.next
    pslow = head
    while pfast and pfast.next:
        pfast = pfast.next.next
        pslow = pslow.next
    return pslow

def merge(left, right):
    dummy = ListNode(0)
    tail = dummy
    
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    if left:
        tail.next = left
    else:
        tail.right = right
    
    return dummy.next

```

# Reference

