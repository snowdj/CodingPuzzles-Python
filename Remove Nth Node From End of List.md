# Problem

http://www.lintcode.com/en/problem/remove-nth-node-from-end-of-list/

Given a linked list, remove the Nth node from the end of list and return its head.

Notice: The minimum number of nodes in list is *n*.

**Example**

Given linked list: ```1->2->3->4->5->null```, and n = ```2```.  
After removing the second node from the end, the linked list becomes ```1->2->3->5->null```. 

# Thoughts

- As the removing might happen on the head node, using a dummy node to simplify the process
- How to remove the Nth node from the end of the list? Use two pointers: fast pointer, and slow pointer
  - Faster pointer: move N times towards the end
  - What happens if N is equal to or larger than the length of the linked list? Then the head element will be removed, so return head.next
  - Then move slow pointer together with faster pointer
  - When faster pointer points to the end (null), slow pointer is at the Nth element from the end
- Delete a node: move the prev pointer's next pointer

# My Solution

```
    def removeNthFromEnd(self, head, n):
        # write your code here
        
        if head.next is None and n == 1:
            return None
        
        fast = head
        slow = head
        
        for i in range(0, n):
            if fast.next is None:
                return head.next
            fast = fast.next
        
        while (fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next
        
        if head == slow:
            head = head.next
        else:
            slow.next = slow.next.next
        
        return head
```

# Reference