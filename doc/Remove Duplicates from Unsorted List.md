# Problem

http://www.lintcode.com/en/problem/remove-duplicates-from-unsorted-list/

Write code to remove duplicates from an unsorted linked list.

**Example**

Given ```1->3->2->1->4```
Return ```1->3->2->4```

# Thoughts

## Method 1
- Use a list to store all values that appeared in the list nodes
- If a node's value exists in the list, skip this node in the list
- If a node's value does not exist in the list, add this value to list
- How to skip a node: pre.next = curr.next

# My Solution

```
    def removeDuplicates(self, head):
        # Write your code here
        if head is None or head.next is None:
            return head
        
        vals = []
        lastHead = None
        start = head
        while head:
            if head.val in vals:
                lastHead.next = head.next
            else:
                vals.append(head.val)
                lastHead = head
            head = head.next
        
        return start
```

Another method

```
    def removeDuplicates(self, head):
        # Write your code here
        mp = dict()
        if head is None:
            return head;
        mp[head.val] = 1
        tail = head;
        now = head.next;
        while now is not None:
            if now.val not in mp:
                mp[now.val] = 1
                tail.next = now
                tail = tail.next
            now = now.next;

        tail.next = None;
        return head;
```

# Reference