# Problem

http://www.lintcode.com/en/problem/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

**Example**

Given ```-21->10->4->5```, tail connects to node index 1, return true

# Thoughts

- Use a fast pointer and slow pointer, fast pointer has 2x speed, slow pointer has 1x speed
- If fast pointer and slow pointer meets, there is a cycle in the linked list
- Note: the while loop condition is (fast.next and fast.next), because fast = fast.next.next in the while loop, fast.next must exist

# My Solution

```
    def hasCycle(head):
        # write your code here
        if head is None or head.next is None:
            return False
        
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False
```
