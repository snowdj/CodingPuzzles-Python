# Problem

http://www.lintcode.com/en/problem/reorder-list/

Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... 

** Example **

Given ```1->2->3->4->null```, reorder it to ```1->4->2->3->null```

# Thoughts

- Cut the one linked list into two linked lists, the cut point is the middle element
- Reverse the second linked list
- Connect the first linked list and the second linked list

# My Solution

```
def reorderList(head):
    if head is None or head.next is None:
        return head
    
    pfast = head
    pslow = head
    while pfast and pfast.next and pfast.next.next:
        pfast = pfast.next.next
        pslow = pslow.next
    
    pfast = pslow.next # put pfast to the head of the second list
    pslow.next = None # cut the two lists
    
    pfast = reverseList(pfast)
    
    # connect two linked lists
    tail = head # head is the head of first list
    while pfast:
        pnext = pfast.next
        pfast.next = tail.next
        tail.next = pfast
        tail = tail.next.next
        pfast = pnext

    return head

def reverseList(head):
    if head is None or head.next is None:
        return head
    
    lastHead = None
    while head:
        lastNext = head.next
        head.next = lastHead
        lastHead = head
        head = lastNext
    
    return lastHead
```

# Reference