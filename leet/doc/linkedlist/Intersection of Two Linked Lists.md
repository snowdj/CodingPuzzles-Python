# Problem

https://leetcode.com/problems/intersection-of-two-linked-lists/description/


Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
```

Notes:

* If the two linked lists have no intersection at all, return null.
* The linked lists must retain their original structure after the function returns.
* You may assume there are no cycles anywhere in the entire linked structure.
* Your code should preferably run in O(n) time and use only O(1) memory.

# Thoughts

1. Calculate the lengths of two linked lists, and find out which one is longer
2. For the longer linked list, go to the (len_long - len_short)'s node, record it as postion Start
3. Now from start to end, two linked lists have the same length. Visit the nodes one by one and compare till the same node is found, which is the intersection node.

# My Solution

```python

def get_list_length(head):
    if head is None:
        return 0
    
    n = 0
    while(head):
        head = head.next
        n += 1
    
    return n

def move_forward_list(head, long_len, short_len):
    move_len = long_len - short_len
    while (head and move_len > 0):
        head = head.next
        move_len -= 1
    return head

def getIntersectionNode(l0, l1):
    if l0 is None or l1 is None:
        return None
    
    l0_len = get_list_length(l0)
    l1_len = get_list_length(l1)
    #print(l0_len)
    #print(l1_len)
    
    if l0_len > l1_len:
        head0 = move_forward_list(l0, l0_len, l1_len)
        head1 = l1
    elif l0_len < l1_len:
        head0 = l0
        head1 = move_forward_list(l1, l1_len, l0_len)
    else:
        head0 = l0
        head1 = l1
    
    result = None
    while(head0 and head1):
        if head0 == head1:
            result = head0
            break
        head0 = head0.next
        head1 = head1.next

    return result
```

# Reference

