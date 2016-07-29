# Problem

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

**Example**
Given ```1->4->3->2->5->2->null```, and x = ```3```,
return ```1->2->2->3->4->5->null```

# Thoughts

- Similar to merge sort
- Use a head1 and head2 as two dummy nodes
- After the while loop, connect phead1 and head2 as: phead1.next = head2.next
- Remove head1, return head1.next

# My Solution

```
def partition(head, x):
    head1 = ListNode(0)
    head2 = ListNode(0)
    tmp = head
    phead1 = head1
    phead2 = head2
    while tmp:
        if tmp.val < x:
            phead1.next = tmp
            tmp = tmp.next
            phead1 = phead1.next
            phead1.next = None
        else:
            phead2.next = tmp
            tmp = tmp.next
            phead2 = phead2.next
            phead2.next = None
    
    phead1.next = head2.next
    head = head1.next
    return head
    

```

# Reference