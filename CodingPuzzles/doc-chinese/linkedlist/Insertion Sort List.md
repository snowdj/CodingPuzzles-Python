# Problem

http://www.lintcode.com/en/problem/insertion-sort-list/

Sort a linked list using insertion sort.

**Example**

Given ```1->3->2->0->null```, return ```0->1->2->3->null```

# Thoughts

- Insertion sort: compare each element with the previous elements

# My Solution

```
    def insertionSortList(self, head):
        # write your code here
        if head is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        
        return dummy.next
```

# Reference

- http://www.cnblogs.com/zuoyuan/p/3700105.html
