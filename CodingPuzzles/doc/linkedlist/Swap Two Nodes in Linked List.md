# Problem

http://www.lintcode.com/en/problem/swap-two-nodes-in-linked-list/

Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, do nothing.

Notice: You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.

**Example**

Given ```1->2->3->4->null``` and v1 = ```2```, v2 = ```4```. 

Return ```1->4->3->2->null```. 

# Thoughts

- Find the two nodes (find prev node, because swapping need change the next pointers of previous nodes)
- Since need find the prev node, using a dummy node (while loop condition: curr.next)
- Swap the two nodes
- Case 1: cannot find n1 and n2, do nothing
- Case 2: cannot find n1 or n2, do nothing
- Case 3: n1 and n2 are adjacent
- Case 4: n1 and n2 are not adjacent
- How to swap? record post nodes

# My Solution

```
    def swapNodes(self, head, v1, v2):
        # Write your code here
        if head is None:
            return head
        
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        p1_pre = None
        p2_pre = None
        
        while curr.next:
            if curr.next.val == v1:
                p1_pre = curr
            if curr.next.val == v2:
                p2_pre = curr
            curr = curr.next
        
        if p1_pre is None or p2_pre is None:
            return dummy.next
        
        if p1_pre == p2_pre:
            return dummy.next
        
        if p1_pre.next == p2_pre:
            node1 = p1_pre.next
            node2 = p2_pre.next
            post2 = node2.next
            
            p1_pre.next = node2
            node2.next = node1
            node1.next = post2
        elif p2_pre.next == p1_pre:
            node1 = p1_pre.next
            node2 = p2_pre.next
            post1 = node1.next
            
            p2_pre.next = node1
            node1.next = node2
            node2.next = post1
        else:
            node1 = p1_pre.next
            post1 = node1.next
            node2 = p2_pre.next
            post2 = node2.next
            
            p1_pre.next = node2
            node2.next = post1
            p2_pre.next = node1
            node1.next = post2
            
        return dummy.next
```