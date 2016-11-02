# Problem

http://www.lintcode.com/en/problem/palindrome-linked-list/

Implement a function to check if a linked list is a palindrome.

**Example**
Given ```1->2->1```, return true

# Thoughts

- Use fast and slow pointers to find the middle point of the linked list
- Reverse the second half of the linked list
- Check if the first half is the same as the second half of the linked list. If true, this linked list is a palindrome list
- How to check first half == second half?

```
while p1 and p1.val == p2.val:
    p1 = p1.next
    p2 = p2.next

if p1 is None:
    return True
else:
    return False
```

- After checking, reconstruct the linked list (optional)

# My Solution

```
    def isPalindrome(self, head):
        # Write your code here
        if head is None:
            return True
        
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        start, last = slow.next, None
        while start:
            next = start.next
            start.next = last
            last, start = start, next
        
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        
        # reconstruct the linked list
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last = p
            p = p.next
            
        slow.next = last
        
        return p1 is None
```

# Reference

- http://bookshadow.com/weblog/2015/07/10/leetcode-palindrome-linked-list/