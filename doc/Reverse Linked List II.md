# Problem

http://www.lintcode.com/en/problem/reverse-linked-list-ii/

Reverse a linked list from position m to n.



# Thoughts

- Find m and n
- The node before m (starting of the reverse) need be updated: node.next = node n
- Start reverse
  - save node.next
  - node.next = lastnode
  - lastnode = node
  - node = saved node.next
  
# My Solution

```
def reverseBetween(head, m, n):
    if head is None or head.next is None:
        return head
    
    dummy = head
    preStart = head
    for i in range(m):
        if i == m-2:
            preStart = head
        head = head.next
    
    start = head
    lastHead = None
    for j in range(m, n):
        lastNext = head.next
        head.next = lastHead
        lastHead = head
        head = lastNext
    
    preStart.next = lastHead
    start.next = head
    
    return dummy

```

# Reference