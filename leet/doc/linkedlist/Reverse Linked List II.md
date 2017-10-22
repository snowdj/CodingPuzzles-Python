# Problem

http://www.lintcode.com/en/problem/reverse-linked-list-ii/

Reverse a linked list from position m to n.

Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list.

# Thoughts

- Find m and n
- The node before m (starting of the reverse) need be updated: node.next = node n
- Start reverse
  - save node.next
  - node.next = lastnode
  - lastnode = node
  - node = saved node.next
  
# My Solution

```python
    def reverseBetween(head, m, n):
        if head is None or m == n:
            return head
    
        first = head
        c = 0
        prev = None
        while (head and c < m-1):
            prev = head
            head = head.next
            c += 1
        new_head = prev
        new_tail = head
        while (head and c <= n-1):
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
            c += 1
        new_tail.next = next_node
                
        if not prev == None:
            prev.next = new_head
        else:
            first = new_head
        
        return first
```

# Reference