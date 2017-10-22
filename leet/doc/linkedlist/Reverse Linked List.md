# Problem

http://www.lintcode.com/en/problem/reverse-linked-list/

Reverse a linked list.

**Example**

Given ```1->2->3```, return the reversed linked list ```3->2->1```. 

# Thoughts

- Save the last node, and change current node's next to last node
- Note: return node is last node, not the original head

1. For each node, save itself as node_prev, save next node to node_next
2. set node.next = node_prev
3. Go to node_next, repeat 1-2

# My Solution

```
def reverse_linkedlist(l0):
    if l0 is None or l0.next is None:
        return l0
    
    head = l0
    newhead = None
    nextnode=None
    while head:
        nextnode = head.next
        head.next = newhead
        newhead = head
        head = nextnode
    
    return newhead
```

# Reference
