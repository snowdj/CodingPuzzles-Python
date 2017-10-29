# Problem

http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

**Example**

Given ```1->1->2```, return ```1->2```. 
Given ```1->1->2->3->3```, return ```1->2->3```. 

# Thoughts

- This problem requires keep only one of the duplicated element
- If current element's next element has the same value as the current, change the next pointer of the current element to skip the next element
- Detail: if curr.next.val == curr.val, no need to move curr to curr.next, because still need compare curr and curr.next.next
- No need use dummy node for this one, because "deleting" operation is ```curr.next = curr.next.next```, no change on current node.

# My Solution

```python
    def deleteDuplicates(head):
        # write your code here
        curr = head                                                        
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
```

# Reference