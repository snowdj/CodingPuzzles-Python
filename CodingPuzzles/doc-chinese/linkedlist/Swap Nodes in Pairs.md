# Problem

http://www.lintcode.com/en/problem/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.

**Example**

Given ```1->2->3->4```, you should return the list as ```2->1->4->3```

# Thoughts

## Method 1
- Add a dummy node
- Swap nodes with a temp node

## Method 2
- Separate the list into two: even nodes and odd nodes
- Combine the two lists back in one

# My Solution

```
def swapPairs(head):
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next and p.next.next:
        tmp = p.next.next
        p.next.next = tmp.next
        tmp.next = p.next
        p.next = tmp
        p = p.next.next
    
    return dummy.next
```

# Reference
