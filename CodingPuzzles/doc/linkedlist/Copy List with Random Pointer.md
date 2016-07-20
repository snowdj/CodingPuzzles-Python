# Problem

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

# Thoughts

- Step 1: Insert a new node after each node in the original list
  - new node value = original node value
  - new node random pointer = original node random pointer (initial)
- Step 2: Mapping the random pointer
  - New node's random pointer = original node random.next
- Note scanning the original node only: tmp = tmp.next.next
- Separate the new nodes in a new linked list (head.next = tmp.next)

# My Solution

```
def copyRandomList(head):
    if head is None:
        return None
    
    tmp = head
    while tmp:
        newNode = RandomListNode(tmp.label)
        newNode.next = tmp.next
        newNode.random = tmp.random
        tmp.next = newNode
        tmp = tmp.next.next
    
    tmp = head
    while tmp:
        if tmp.random:
            tmp.next.random = tmp.random.next
        tmp = tmp.next.next
    
    newhead = head.next
    while head:
        tmp = head.next
        head.next = tmp.next
        head = head.next
        if tmp.next:
            tmp.next = tmp.next.next
    
    return newhead
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3745126.html
