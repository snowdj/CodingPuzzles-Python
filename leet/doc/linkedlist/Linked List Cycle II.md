# Problem 

http://www.lintcode.com/en/problem/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins.

If there is no cycle, return ```null```. 

**Example**

Given ```-21->10->4->5```, tail connects to node index 1, return ```10```


# Thoughts

- If a linked list has a cycle, fast pointer and slow pointer can meet at some point
- After the two pointers meet, slow pointer goes back to head, then move fast pointer and slow pointer together. When they meet again, the point is the start of the cycle

# My Solution

```python
def detectCycle(head):
    if head == None or head.next == None:
        return head
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break
    if slow == fast:
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    return None
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3701877.html